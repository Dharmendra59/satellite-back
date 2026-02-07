import torch
from lstm_model import OrbitLSTM

model = OrbitLSTM()
optimizer = torch.optim.Adam(model.parameters())
loss_fn = torch.nn.MSELoss()

dummy_x = torch.rand((100, 10, 6))
dummy_y = torch.rand((100, 3))

for _ in range(10):
    pred = model(dummy_x)
    loss = loss_fn(pred, dummy_y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

torch.save(model.state_dict(), "orbit_lstm.pth")
print("LSTM trained & saved")
