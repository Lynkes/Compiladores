##Analise de Instruções (calculo de instruções de atribuição e comparação)
import matplotlib.pyplot as plt
import time

def your_algorithm(data):
    def vector_multiply(v1, v2):
        result = 0
        for i in range(len(v1)):
            result += v1[i] * v2[i]
        return result
    # 1+N+1+1+1
    pass

def matrix_vector_multiply(matrix, vector):
    result = [0] * len(vector)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

# 1+n+1(n+1+1+1)

def matrix_multiply(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# 1+n+1(n+1(n+1+1+1))



if __name__ == "__main__":
    data_sizes = [10, 100, 1000, 10000] # List of data sizes to test
    times = [] # List to store the execution times
    start_time = time.time() # Record the start time
    your_algorithm(): # Call your algorithm with the generated data
    end_time = time.time() # Record the end time
    times.append(end_time - start_time) # Calculate and store the execution time

# Plot the graph
plt.plot(data_sizes, times)
plt.xlabel('Data Size')
plt.ylabel('Execution Time (s)')
plt.title('Algorithmic Complexity')
plt.show()