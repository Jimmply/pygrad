### torch gradient
import torch

# f = w * x

# f2 = 2 * x

X = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
Y = torch.tensor([2, 4, 6, 8, 10], dtype=torch.float32)

w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

#model pred
def forward(x):
    return w * x

#model loss
def loss(y, y_predicted):
    return ((y_predicted - y)**2).mean()

#gradient
#loss MSE = 1/N * (w*x - y)**2
#dJ/dw = 1/N * 2x * (w*x - y)
def gradient(x, y, y_predicted):
    return np.dot(2*x, y_predicted-y).mean()

print(f'Prediction before training: f(5) = {forward(5):.3f}')

#Training
learning_rate = 0.01
n_iters = 10

for epoch in range(n_iters):
    #prediction = forward pass
    y_pred = forward((X))

    #loss
    l = loss(Y, y_pred)

    #gradients = backward pass
    l.backward() # dl/dw

    #update weight
    with torch.no_grad():
        w -= learning_rate * w.grad

    #zero gradients
    w.grad.zero_()

    if epoch % 1 == 0:
        print(f'epoch {epoch+1}: w = {w:.3f}, loss = {l:.8f}')

print(f'Prediction after training: f(5) = {forward(5):.3f}')