
import tensorflow as tf
import tensorflow.keras.layers as tfl

def functional_convolutional_model(input_shape):
    """
    Constructs a convolutional neural network model using the Functional API of TensorFlow Keras.
    
    This model includes two convolutional layers each followed by a ReLU activation and max pooling,
    and concludes with a fully connected dense layer. The network architecture is designed for image
    classification tasks and is structured as follows:
    CONV2D -> RELU -> MAXPOOL -> CONV2D -> RELU -> MAXPOOL -> FLATTEN -> DENSE
    
    Note: The stride, kernel sizes, and other parameters are hard-coded for demonstration purposes.
    In a typical application, these would be configurable parameters.

    Parameters:
    - input_shape (tuple): The shape of the input data (height, width, channels).

    Returns:
    - model (tf.keras.Model): A TensorFlow Keras model instance configured with the network architecture.
    """

    # Input layer specifying the shape of the input
    input_img = tf.keras.Input(shape=input_shape)
    
    # First convolutional layer with 8 filters of size 4x4, using 'same' padding to preserve dimensions
    Z1 = tfl.Conv2D(filters=8, kernel_size=(5,5), padding="same", strides=1)(input_img)
    # Activation layer applying the ReLU function to introduce non-linearity
    A1 = tfl.ReLU()(Z1)
    # First pooling layer using max pooling with a 8x8 window and stride of 8
    P1 = tfl.MaxPooling2D(pool_size=(8,8), strides=8, padding="same")(A1)
    
    # Second convolutional layer with 16 filters of size 2x2, using 'same' padding to preserve dimensions
    Z2 = tfl.Conv2D(filters=16, kernel_size=(3,3), padding="same", strides=1)(P1)
    # Activation layer applying the ReLU function
    A2 = tfl.ReLU()(Z2)
    # Second pooling layer using max pooling with a 4x4 window and stride of 4
    P2 = tfl.MaxPooling2D(pool_size=(4,4), strides=4, padding="same")(A2)
    
    # Flatten layer to convert the 3D outputs to 1D vector before feeding into the dense layer
    F = tfl.Flatten()(P2)
    # Dense layer with 6 output units for classification (assuming 6 classes) with softmax activation
    outputs = tfl.Dense(units=6, activation="softmax")(F)
    
    # Create the model object linking inputs and outputs
    model = tf.keras.Model(inputs=input_img, outputs=outputs)
    return model


        
