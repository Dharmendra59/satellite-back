import torch
from lstm_model import OrbitLSTM

model = OrbitLSTM()
model.load_state_dict(torch.load("orbit_lstm.pth"))
model.eval()

x = torch.rand((1, 10, 6))
y = model(x)
print("Future position:", y.detach().numpy())
