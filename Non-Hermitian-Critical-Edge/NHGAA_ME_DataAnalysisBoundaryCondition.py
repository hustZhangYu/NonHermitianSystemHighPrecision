# some functions to analyze the data

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from data_io import load_data, parse_complex_string





def EigenvaluesWithBoundaryCondition():
    data = load_data('C:/Users/Lenovo/OneDrive/A_CodePython/NHGAA/EigenvalueData_BoundaryConditionH.csv')
    print(data.shape)
    for i in range(data.shape[0]):
        m = data.loc[i].values
        m1 = np.array([parse_complex_string(str(val).strip("'")) for val in m])
        colors = plt.cm.viridis(i / data.shape[0])  # 使用viridis颜色映射创建渐变色
        plt.plot(np.real(m1), np.imag(m1), 'o', color=colors,markersize=5)

    E=np.linspace(-1,1,100)*np.exp(1j*np.pi*0)
    plt.plot(np.real(E),np.imag(E),'-',linewidth=3)
    plt.xlabel('Re(E)')
    plt.ylabel('Im(E)')
    plt.title('Eigenvalues with Boundary Condition')
    plt.savefig('EigenvaluesWithBoundaryConditionL_89_v_1.png')
    plt.show()

def EigenvaluesWithBoundaryConditionSingleParameter():
    data = load_data('C:/Users/Lenovo/OneDrive/A_CodePython/NHGAA/EigenvalueData_BoundaryConditionH.csv')
    print(data.shape)
    i=0 
    m = data.loc[i].values
    m1 = np.array([parse_complex_string(str(val).strip("'")) for val in m])
    colors = plt.cm.viridis(i / data.shape[0])  # 使用viridis颜色映射创建渐变色
    plt.plot(np.real(m1), np.imag(m1), 'o', color=colors,markersize=5)

    E=np.linspace(-1,1,100)*np.exp(1j*np.pi*0)
    plt.plot(np.real(E),np.imag(E),'-',linewidth=3)
    plt.xlabel('Re(E)')
    plt.ylabel('Im(E)')
    plt.title('Eigenvalues with Boundary Condition')
    plt.savefig('EigenvaluesWithBoundaryConditionSingleParameter_v_1.png')
    plt.show()

if __name__ == "__main__":
    EigenvaluesWithBoundaryCondition()
#   EigenvaluesWithBoundaryConditionSingleParameter()
