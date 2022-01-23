import torch.nn as nn
import torch
class BasicGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size, dropout_prob, directions=1):
        super(BasicGRU, self).__init__()
        print("Building Basic GRU model....")
    
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        self.directions = directions
        self.dropout = nn.Dropout(dropout_prob)
        self.gru = nn.GRU(input_size, self.hidden_size, num_layers=self.num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_size, output_size)
        
    def forward(self, x, states):
        x, (h, c) = self.gru(x, states)
        out = self.linear(x)
        return out, (h, c)
    
    def init_hidden_states(self, batch_size):
        state_dim = (self.num_layers * self.directions, batch_size, self.hidden_size)
        return (torch.zeros(state_dim).to(device), torch.zeros(state_dim).to(device))
    
    def _init_state(self, batch_size=1):
        weight = next(self.parameters()).data  # nn.GRU의 가중치 텐서 추출
        return weight.new(self.n_layers, batch_size, self.hidden_dim).zero_()  # 같은 크기의 tensor 제작 후 0으로 변환
    
    
    
model_GRU = BasicGRU(1, 256, vocab_size, 128, n_classes, 0.5).to(DEVICE)
model = BasicGRU(NUM_FEATURES, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE, DROPOUT).to(device)
optimizer_GRU = torch.optim.Adam(model_GRU.parameters(), lr=lr)


def save_checkpoint(epoch, min_val_loss, model_state, opt_state):
    #     print(f"New minimum reached at epoch #{epoch + 1}, saving model state...")
    checkpoint = {'epoch': epoch + 1, 'min_val_loss': min_val_loss, 
                  'model_state': model_state, 'opt_state': opt_state,} 
    torch.save(checkpoint, "./model_state.pt")


def load_checkpoint(path, model, optimizer):
    # load check point
    checkpoint = torch.load(path)
    min_val_loss = checkpoint["min_val_loss"]
    model.load_state_dict(checkpoint["model_state"])
    optimizer.load_state_dict(checkpoint["opt_state"])
    return model, optimizer, checkpoint["epoch"], min_val_loss


def training(model, epochs, validate_every=2):

    training_losses = []
    validation_losses = []
    min_validation_loss = np.Inf

    # Set to train mode
    model.train()

    for epoch in tqdm(range(epochs)):
        # Initialize hidden and cell states with dimension:
        # (num_layers * num_directions, batch, hidden_size)
        states = model.init_hidden_states(BATCH_SIZE)
        running_training_loss = 0.0

        # Begin training
        for idx, (x_batch, y_batch) in enumerate(training_dl):
            # Convert to Tensors
            x_batch = x_batch.float().to(device)
            y_batch = y_batch.float().to(device)
            # Truncated Backpropagation
            states = [state.detach() for state in states]          

            optimizer.zero_grad()

            # Make prediction
            output, _ = model(x_batch, states)

            # Calculate loss
            loss = criterion(output[:, -1, :], y_batch)
            loss.backward()
            running_training_loss += loss.item()

            torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)
            optimizer.step()

        # Average loss across timesteps
        training_losses.append(running_training_loss / len(training_dl))
        
        
        if epoch % validate_every == 0:
            # Set to eval mode
            model.eval()

            validation_states = model.init_hidden_states(BATCH_SIZE)
            running_validation_loss = 0.0

            for idx, (x_batch, y_batch) in enumerate(validation_dl):
                
                # Convert to Tensors
                x_batch = x_batch.float().to(device)
                y_batch = y_batch.float().to(device)

                validation_states = [state.detach() for state in validation_states]
                output, validation_states = model(x_batch, validation_states)
                validation_loss = criterion(output[:, -1, :], y_batch)
                running_validation_loss += validation_loss.item()
                
        validation_losses.append(running_validation_loss / len(validation_dl))
        # Reset to training mode
        model.train()

        is_best = running_validation_loss / len(validation_dl) < min_validation_loss

        if is_best:
            min_validation_loss = running_validation_loss / len(validation_dl)
            save_checkpoint(epoch + 1, min_validation_loss, model.state_dict(), optimizer.state_dict())
        

    # Visualize loss
    epoch_count = range(1, len(training_losses) + 1)
    plt.plot(epoch_count, training_losses, 'r--')
    plt.legend(['Training Loss'])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()

    val_epoch_count = range(1, len(validation_losses) + 1)
    plt.plot(val_epoch_count, validation_losses, 'b--')
    plt.legend(['Validation loss'])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()