import numpy as np
from load_utils import load_matrix
cases = [
    ((120,750),None, "None"),
    ((120,750), (750,), "(750,)"),
    ((120,750),(120,1),"(120,1)"),
    ((120,750),(1,750),"(1,750)"),
    ((120,750),(120,),"(120,)"),
    ((120,750), (100,),"(100,)"),
]

for a_shape, b_shape, label in cases :
    arr_a = np.ones(a_shape)
    arr_b = 2.0 if b_shape is None else np.ones(b_shape)
    
    try :
        result = (arr_a + arr_b).shape
    except ValueError :
        result = "Error!"
        
    print(f"{a_shape} + {b_shape} : {result}")
    
matrix = load_matrix()

means_w = matrix.mean(axis=1)

means = matrix.mean(axis=1, keepdims=True)
print(f"{(matrix - means).shape}")
print(f"{(matrix - means)}")

# (120,)

# 브로드카