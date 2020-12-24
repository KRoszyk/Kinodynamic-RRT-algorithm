import numpy as np
import math


class RRT:
    def __init__(self, map, start_state, goal_state, initial_control):
        self.map = map
        self.height = np.shape(map)[0]
        self.width = np.shape(map)[1]
        self.start_state = start_state
        self.goal_state = goal_state
        self.vertices = {self.start_state: {'Parent': None, 'Control': initial_control}}
        self.delta_t = 10
        self.T = 100
        self.L = 50

    def random_state(self):
        x = int(self.width * np.random.random_sample())
        y = int(self.start_state[1] * np.random.random_sample())
        theta = (2 * np.random.random_sample() - 1) * np.pi
        random_state = (x, y, theta)
        return random_state

    def check_if_valid(self, pos):
        if pos[0] >= self.width or pos[1] >= self.height or pos[0] < 0 or pos[1] < 0 or self.map[pos[1], pos[0]] == 0:
            return False
        else:
            return True

    def calculate_metrics(self, state1, state2, gamma):
        alfa = 1
        beta = 1
        metrics = pow(alfa * pow((state1[0] - state2[0]), 2) + beta * pow((state1[1] - state2[1]), 2) + gamma * pow(
            (state1[2] - state2[2]), 2), 0.5)
        return metrics

    def find_closest_state(self, pos):
        metrics_min = math.sqrt(self.width ** 2 + self.height ** 2)
        for key in self.vertices.keys():
            metrics = self.calculate_metrics(pos, key, 20)
            if metrics < metrics_min:
                closest = key
                metrics_min = metrics
        return closest

    def random_control(self):
        v_lin = np.random.random_sample()
        turn_angle = (2 * np.random.random_sample() - 1) * np.pi / 4
        return v_lin, turn_angle

    def new_state(self, u, xk):
        x_new = u[0] * np.sin(xk[2]) * self.delta_t + xk[0]
        y_new = xk[1] - u[0] * np.cos(xk[2]) * self.delta_t
        theta_new = (u[0] / self.L) * np.tan(u[1]) * self.delta_t + xk[2]
        new_state = (int(x_new), int(y_new), theta_new)
        return new_state

    def extend(self, xnear, xrand):
        metrics_ref = 25
        metrics_max = self.calculate_metrics(xnear, xrand, 20)
        current_state = xnear
        u = self.random_control()
        for iter in range(0, int(self.T / self.delta_t)):
            x_new = self.new_state(u, current_state)
            if self.check_if_valid(x_new):
                if self.calculate_metrics(x_new, xrand, 20) < metrics_max:
                    if self.calculate_metrics(x_new, xrand, 20) <= metrics_ref or iter == self.T / self.delta_t - 1:
                        self.vertices[x_new] = {}
                        self.vertices[x_new]['Parent'] = xnear
                        self.vertices[x_new]['Control'] = u
                        return x_new
                    current_state = x_new
                    metrics_max = self.calculate_metrics(current_state, xrand, 20)
            else:
                return None

    def search(self):
        endReached = False
        startReached = False
        prox = 100
        path = []
        controls = []
        while not endReached:
            if not self.check_if_valid(self.start_state):
                break
            xrand = self.random_state()
            xnear = self.find_closest_state(xrand)
            xnew = self.extend(xnear, xrand)
            if len(self.vertices) > 50:
                self.vertices.clear()
                path.append((self.start_state[0], self.start_state[1], 0))
                path.append((self.goal_state[0], self.goal_state[1], 0))
                startReached = True
                break
            if xnew is not None:
                if self.calculate_metrics(xnew, self.goal_state, 20) <= prox:
                    self.vertices[xnew] = {}
                    self.vertices[xnew]['Parent'] = xnear
                    self.vertices[xnew]['Control'] = (0, 0)
                    endReached = True
                    considered_node = xnew
                    path.append(considered_node)
        while not startReached:
            considered_node = self.vertices[considered_node]['Parent']
            path.append(considered_node)
            controls.append(self.vertices[considered_node]['Control'])
            if considered_node[0] == self.start_state[0] and considered_node[1] == self.start_state[1]:
                startReached = True
        path_to_draw = [(i[0], i[1]) for i in path]
        angles = [i[2] for i in path]
        all_points = [(i[0], i[1]) for i in self.vertices.keys()]
        controls.reverse()

        return path_to_draw, all_points, controls, angles
