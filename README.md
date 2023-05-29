# EpilepsyDetection
Epilepsy seizure detection in EEG signal using Deep Learning methods
![image](https://github.com/harshyadav1508/EpilepsyDetection/assets/55807854/d3bc196e-4868-423e-adf5-45dbd7339bee)

- EEG data is first passed through an LSTM layer of 80 neurons. (helps in learning short and long-term dependencies between the EEG )

- Output of LSTM is passed to fully connected dense layer (50 units) to translate the information learned by the LSTM layer into meaningful seizure-associated features. 

- Output of the FC layer is passed through a one-dimensional average pooling layer. The motivation for this was that all the EEG segments should contribute equally to the label prediction. 

- The output of the average pooling layer is then presented as an input to the softmax layer for EEG classification. 

