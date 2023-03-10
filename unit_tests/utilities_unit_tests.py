import sys, torch
sys.path.append(".")
from models import utilities

def test_to_batches_of_instances_A():
    x = torch.arange(start=0, end=28, step=1).reshape(shape=(7,4))
    y = torch.arange(start=0, end=24, step=1).reshape(shape=(2,3,4))
    y_hat = utilities.reshape_by_time_frame_count(x=x, time_frames_per_instance=3)

    if torch.equal(y, y_hat): print("\tPassed unit test A for to_batches_of_instances.")
    else: print("\tFailed unit test A for to_batches_of_instances.")

def test_reshape_by_label_A():
    x = torch.arange(0,200,1).reshape(shape=(20,10))
    y = torch.arange(0,40,1).reshape(shape=(20,2))
    labels = [""] + ["A"] * 2 + [""] * 1 + ["B"] * 3 + [""] * 2 + ["C"] * 9 + [""] * 2
    
    x_expected = torch.Tensor(
        [[[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 10.,  11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.], [ 20.,  21.,  22.,  23.,  24.,  25.,  26.,  27.,  28.,  29.], [ 30.,  31.,  32.,  33.,  34.,  35.,  36.,  37.,  38.,  39.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 40.,  41.,  42.,  43.,  44.,  45.,  46.,  47.,  48.,  49.], [ 50.,  51.,  52.,  53.,  54.,  55.,  56.,  57.,  58.,  59.], [ 60.,  61.,  62.,  63.,  64.,  65.,  66.,  67.,  68.,  69.], [ 70.,  71.,  72.,  73.,  74.,  75.,  76.,  77.,  78.,  79.], [ 80.,  81.,  82.,  83.,  84.,  85.,  86.,  87.,  88.,  89.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 90.,  91.,  92.,  93.,  94.,  95.,  96.,  97.,  98.,  99.], [100., 101., 102., 103., 104., 105., 106., 107., 108., 109.], [110., 111., 112., 113., 114., 115., 116., 117., 118., 119.], [120., 121., 122., 123., 124., 125., 126., 127., 128., 129.], [130., 131., 132., 133., 134., 135., 136., 137., 138., 139.], [140., 141., 142., 143., 144., 145., 146., 147., 148., 149.], [150., 151., 152., 153., 154., 155., 156., 157., 158., 159.], [160., 161., 162., 163., 164., 165., 166., 167., 168., 169.], [170., 171., 172., 173., 174., 175., 176., 177., 178., 179.], [180., 181., 182., 183., 184., 185., 186., 187., 188., 189.], [190., 191., 192., 193., 194., 195., 196., 197., 198., 199.]]]
    )

    y_expected = torch.Tensor(
        [[[  0.,  1.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[ 2.,  3.], [ 4.,  5.], [ 6.,  7.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[ 8.,  9.], [10., 11.], [12., 13.], [14., 15.], [16., 17.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[18., 19.], [20., 21.], [22., 23.], [24., 25.], [26., 27.], [28., 29.], [30., 31.], [32., 33.], [34., 35.], [36., 37.], [38., 39.]]]
    )
    x_predicted, y_predicted = utilities.reshape_by_label(x=x,y=y,labels=labels,pause_string="")
  
    if x_expected.size() == x_predicted.size() and torch.equal(x_expected, x_predicted) and y_expected.size() == y_predicted.size() and torch.equal(y_expected, y_predicted):
        print("\tPassed unit test A for reshape_by_label.")
    else: print("\tFailed unit test A for reshape_by_label.")

def test_reshape_by_label_B():
    x = torch.arange(0,200,1).reshape(shape=(20,10))
    labels = [""] + ["A"] * 2 + [""] * 1 + ["B"] * 3 + [""] * 2 + ["C"] * 9 + [""] * 2
    
    x_expected = torch.Tensor(
    [[[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 10.,  11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.], [ 20.,  21.,  22.,  23.,  24.,  25.,  26.,  27.,  28.,  29.], [ 30.,  31.,  32.,  33.,  34.,  35.,  36.,  37.,  38.,  39.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 40.,  41.,  42.,  43.,  44.,  45.,  46.,  47.,  48.,  49.], [ 50.,  51.,  52.,  53.,  54.,  55.,  56.,  57.,  58.,  59.], [ 60.,  61.,  62.,  63.,  64.,  65.,  66.,  67.,  68.,  69.], [ 70.,  71.,  72.,  73.,  74.,  75.,  76.,  77.,  78.,  79.], [ 80.,  81.,  82.,  83.,  84.,  85.,  86.,  87.,  88.,  89.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 90.,  91.,  92.,  93.,  94.,  95.,  96.,  97.,  98.,  99.], [100., 101., 102., 103., 104., 105., 106., 107., 108., 109.], [110., 111., 112., 113., 114., 115., 116., 117., 118., 119.], [120., 121., 122., 123., 124., 125., 126., 127., 128., 129.], [130., 131., 132., 133., 134., 135., 136., 137., 138., 139.], [140., 141., 142., 143., 144., 145., 146., 147., 148., 149.], [150., 151., 152., 153., 154., 155., 156., 157., 158., 159.], [160., 161., 162., 163., 164., 165., 166., 167., 168., 169.], [170., 171., 172., 173., 174., 175., 176., 177., 178., 179.], [180., 181., 182., 183., 184., 185., 186., 187., 188., 189.], [190., 191., 192., 193., 194., 195., 196., 197., 198., 199.]]]
    )

    x_predicted = utilities.reshape_by_label(x=x,labels=labels,pause_string="")
    
    if x_expected.size() == x_predicted.size() and torch.equal(x_expected, x_predicted):
        print("\tPassed unit test B for reshape_by_label.")
    else: print("\tFailed unit test B for reshape_by_label.")

def test_undo_reshape_by_label_A():
    labels = [""] + ["A"] * 2 + [""] * 1 + ["B"] * 3 + [""] * 2 + ["C"] * 9 + [""] * 2
    
    x = torch.Tensor(
        [[[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 10.,  11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.], [ 20.,  21.,  22.,  23.,  24.,  25.,  26.,  27.,  28.,  29.], [ 30.,  31.,  32.,  33.,  34.,  35.,  36.,  37.,  38.,  39.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 40.,  41.,  42.,  43.,  44.,  45.,  46.,  47.,  48.,  49.], [ 50.,  51.,  52.,  53.,  54.,  55.,  56.,  57.,  58.,  59.], [ 60.,  61.,  62.,  63.,  64.,  65.,  66.,  67.,  68.,  69.], [ 70.,  71.,  72.,  73.,  74.,  75.,  76.,  77.,  78.,  79.], [ 80.,  81.,  82.,  83.,  84.,  85.,  86.,  87.,  88.,  89.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.], [  0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.]],
        [[ 90.,  91.,  92.,  93.,  94.,  95.,  96.,  97.,  98.,  99.], [100., 101., 102., 103., 104., 105., 106., 107., 108., 109.], [110., 111., 112., 113., 114., 115., 116., 117., 118., 119.], [120., 121., 122., 123., 124., 125., 126., 127., 128., 129.], [130., 131., 132., 133., 134., 135., 136., 137., 138., 139.], [140., 141., 142., 143., 144., 145., 146., 147., 148., 149.], [150., 151., 152., 153., 154., 155., 156., 157., 158., 159.], [160., 161., 162., 163., 164., 165., 166., 167., 168., 169.], [170., 171., 172., 173., 174., 175., 176., 177., 178., 179.], [180., 181., 182., 183., 184., 185., 186., 187., 188., 189.], [190., 191., 192., 193., 194., 195., 196., 197., 198., 199.]]]
    )

    y = torch.Tensor(
        [[[  0.,  1.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[ 2.,  3.], [ 4.,  5.], [ 6.,  7.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[ 8.,  9.], [10., 11.], [12., 13.], [14., 15.], [16., 17.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[18., 19.], [20., 21.], [22., 23.], [24., 25.], [26., 27.], [28., 29.], [30., 31.], [32., 33.], [34., 35.], [36., 37.], [38., 39.]]]
    )

    x_expected = torch.arange(0,200,1, dtype=torch.float32).reshape(shape=(20,10))
    y_expected = torch.arange(0,40,1, dtype=torch.float32).reshape(shape=(20,2))
  
    x_predicted, y_predicted = utilities.undo_reshape_by_label(y=y,labels=labels,pause_string="",x=x)
    
    if x_expected.size() == x_predicted.size() and torch.equal(x_expected, x_predicted) and y_expected.size() == y_predicted.size() and torch.equal(y_expected, y_predicted):
        print("\tPassed unit test A for undo_reshape_by_label.")
    else: print("\tFailed unit test A for undo_reshape_by_label.")

def test_undo_reshape_by_label_B():
    labels = [""] + ["A"] * 2 + [""] * 1 + ["B"] * 3 + [""] * 2 + ["C"] * 9 + [""] * 2
  
    y = torch.Tensor(
        [[[  0.,  1.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[ 2.,  3.], [ 4.,  5.], [ 6.,  7.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[ 8.,  9.], [10., 11.], [12., 13.], [14., 15.], [16., 17.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.], [ 0.,  0.]],
        [[18., 19.], [20., 21.], [22., 23.], [24., 25.], [26., 27.], [28., 29.], [30., 31.], [32., 33.], [34., 35.], [36., 37.], [38., 39.]]]
    )

    y_expected = torch.arange(0,40,1, dtype=torch.float32).reshape(shape=(20,2))
    
    y_predicted = utilities.undo_reshape_by_label(y=y,labels=labels,pause_string="")
    
    if y_expected.size() == y_predicted.size() and torch.equal(y_expected, y_predicted):
        print("\tPassed unit test B for undo_reshape_by_label.")
    else: print("\tFailed unit test B for undo_reshape_by_label.")

def test_stack_x_A():
    x = torch.arange(start=0, end=30, step=1).reshape(shape=(2,3,5))
    y_hat = utilities.stack_x(x=x, shift_count=3, shift_step_size=2)
    y = torch.Tensor([[[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.,  2.,  3., 4.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  5.,  6.,  7.,  8., 9.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  1.,  2.,  3.,  4., 10., 11., 12., 13., 14.]],

        [[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 15., 16., 17., 18., 19.],
         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 20., 21., 22., 23., 24.],
         [ 0.,  0.,  0.,  0.,  0., 15., 16., 17., 18., 19., 25., 26., 27., 28., 29.]]])
    
    if torch.equal(y, y_hat): print("\tPassed unit test A for stack_x.")
    else: print("\tFailed unit test A for stack_x.")

def test_zero_pad_sequences_A():

    # Create some data
    sequences = [torch.ones(size=[7,13,5]),
                torch.ones(size=[6,17,2]),
                torch.ones(size=[2,11,1])]
    
    # Get prediction
    output = utilities.zero_pad_sequences(sequences=sequences, axis=1)

    # Check whether they all kep their size along the other axes
    valid = True
    for t, tensor in enumerate(output):
        valid = valid and (sequences[t].size()[0] == tensor.size()[0]) and (sequences[t].size()[2] == tensor.size()[2])

    # Check whether the target axes now matches
    time_frame_count = sequences[0].size()[1]
    for tensor in output[1:]:
        valid = valid and (tensor.size()[1] == time_frame_count)

    # Evaluate
    print("\tPassed" if valid else "\tFailed", "unit test A for zero_pad_sequences.")

if __name__ == "__main__":
    print("\nUnit tests for models.utilities.")
    test_to_batches_of_instances_A()
    test_reshape_by_label_A()
    test_reshape_by_label_B()
    test_undo_reshape_by_label_A()
    test_undo_reshape_by_label_B()
    test_stack_x_A()
    test_zero_pad_sequences_A()