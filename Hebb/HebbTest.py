def transpose_array(array):
    return [1 / array[i] for i in range(len(array))]

def get_scalar(f, s):
    return sum([f[i] * s[i] for i in range(len(f))])

def hebb_rule_to_get_weights(result, x0, x1, x2):
    weights = []
    vectors = [transpose_array(x0), transpose_array(x1), transpose_array(x2)]
    for i in range(len(vectors)):
        weights.append(get_scalar(result, vectors[i]) / len(result))
    return weights

def sign_function(array):
    result = []
    for i in range(len(array)):
        if array[i] > 0:
            result.append(1)
        else:
            result.append(-1)
    return result

def get_weighted_sum(weights, x1, x2):
    new_array = []
    for i in range(len(x1)):
        temp_arr = get_scalar(weights,[1,x1[i], x2[i]])
        new_array.append(temp_arr)
    return new_array

def get_result(weights, x1, x2):
    arr = get_weighted_sum(weights, x1, x2)
    return sign_function(arr)

x0, x1, x2, f = [1,1,1,1], [1,1,-1,-1], [1,-1,1,-1], [1,-1,-1,-1]
weights = hebb_rule_to_get_weights(f,x0,x1,x2)
print("Weights: {0}".format(weights))
print("Output: {0}".format(get_result(weights,x1,x2)))
