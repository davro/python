import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Read data from CSV file
data = pd.read_csv("~/workspace/data/csv/bitcoin-weekly.csv")

# Convert data to numpy array
#data_array = data.values

# Exclude non-numeric columns (like date) from scaling
numeric_data = data.drop(columns=['Date'])

# Scale only the numeric columns
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(numeric_data)

# Print the scaled data
#print(scaled_data)


# Normalize data
#scaler = MinMaxScaler(feature_range=(0, 1))
#scaled_data = scaler.fit_transform(data_array)

# Define sequence length
seq_length = 5  # You can adjust this

# Create sequences
sequences = []
for i in range(len(scaled_data) - seq_length):
    sequences.append(scaled_data[i:i+seq_length+1])

# Convert sequences to numpy array
sequences = np.array(sequences)

# Split data into features and target
X = sequences[:, :-1]
y = sequences[:, -1][:,-1]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert data to PyTorch tensors
X_train = torch.from_numpy(X_train).float()
y_train = torch.from_numpy(y_train).float()
X_test = torch.from_numpy(X_test).float()
y_test = torch.from_numpy(y_test).float()

# Define LSTM model
class LSTM(nn.Module):
    def __init__(self, input_size=8, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size
        self.lstm = nn.LSTM(input_size, hidden_layer_size)
        self.linear = nn.Linear(hidden_layer_size, output_size)
        self.hidden_cell = (torch.zeros(1,1,self.hidden_layer_size),
                            torch.zeros(1,1,self.hidden_layer_size))

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq) ,1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]

# Initialize model
model = LSTM()

# Define loss function and optimizer
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train model
epochs = 150
for i in range(epochs):
    for seq, labels in zip(X_train, y_train):
        optimizer.zero_grad()
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                        torch.zeros(1, 1, model.hidden_layer_size))

        y_pred = model(seq)

        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()

    if i%25 == 1:
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')

# Make predictions
with torch.no_grad():
    test_seq = X_test[0]
    test_seq = test_seq.view(-1, 1, 8)
    model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
                    torch.zeros(1, 1, model.hidden_layer_size))
    print(model(test_seq).item(), y_test[0].item())

