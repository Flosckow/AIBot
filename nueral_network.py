import asyncio
# import tensorflow as tf
# import matplotlib as mpl
# import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
# from matplotlib import pyplot

# series = pd.Series.from_csv('daily-total-female-births.csv', header=0)
# print(series.head())
# series.plot()
# plt.show()

inputs = [0,1,0,0]
weight = [0,0,0,0]
desired_result = 1
learning_rate = 0.2
trials = 6


class Perceptron():
    def __init__(self, inputs_vector, weight_vector, actual, desired, learning_rate, trials) -> None:
        self.inputs_vector = inputs_vector
        self.weight_vector = weight_vector
        self.actual = actual
        self.desired = desired
        self.learning_rate = learning_rate
        self.trials = trials

    def __repr__(self) -> str:
        return 'This is Perceptron'

    async def evualate(self):
        """Принимает на вход значения входные и веса  возвращает результат"""
        result = 0
        for input in range(len(self.inputs_vector)):
            layer_value = self.inputs_vector[input] * self.weight_vector[input]
            result += layer_value
        print("evaluate_neural_network: " + str(result))
        print("weights: " + str(self.weight_vector))
        return result
    
    async def evualate_error(self) -> str:
        """Ошибка обработка"""
        error = self.desired - self.actual
        return error

    async def learn(self):
        """Обучение нейронки"""
        for i in range(len(self.inputs_vector)):
            if self.inputs_vector[i] > 0:
                self.weight_vector[i] += self.learning_rate

    async def train(self):
        for i in range(self.trials):
            nueral_net_result = await self.evualate()
            await self.learn()
        


async def main():
    perceptron = Perceptron(inputs_vector=inputs, weight_vector=weight, actual=0, desired=desired_result, learning_rate=learning_rate, trials=trials)
    await perceptron.train()
    


loop = asyncio.get_event_loop()
loop.run_until_complete(main())




    