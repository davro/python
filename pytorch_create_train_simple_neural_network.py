import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(2, 1)  # 2 input features, 1 output

    def forward(self, x):
        x = self.fc(x)
        return x

# Create a sample dataset
data = torch.tensor([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
labels = torch.tensor([[2.0], [3.0], [4.0]])

# Initialize the model, loss function, and optimizer
model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(data)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    print(f'Epoch [{epoch + 1}/100], Loss: {loss.item()}')

# Make predictions
test_data = torch.tensor([[4.0, 5.0]])
predictions = model(test_data)
print(f'Prediction: {predictions.item()}')
