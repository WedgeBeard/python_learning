def get_normalized(num, input_max, input_min, out_range_min, out_range_max):
    return round((((num - input_min) / (input_max - input_min)) * (out_range_max - out_range_min)) + out_range_min, 2)