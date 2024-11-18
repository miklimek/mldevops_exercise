import wandb

epochs = 10
lr = 0.01
# Initialize wandb
run = wandb.init(
    # Set the project where this run will be logged
    project="my-project",
    # Track hyperparameters and run metadata
    config={
        "learning_rate": lr,
        "epochs": epochs,
    },
)

# Simulate training
for epoch in range(epochs):
    training_loss = 0.01 * (epochs - epoch)  # Simulated training loss
    validation_loss = 0.02 * (epochs - epoch)  # Simulated validation loss

    # Log metrics
    wandb.log(
        {
            "epoch": epoch,
            "training_loss": training_loss,
            "validation_loss": validation_loss,
        }
    )

# Log code as an artifact
artifact = wandb.Artifact("example_code", type="code")
artifact.add_file("wandb_example.py")
wandb.log_artifact(artifact)

# Finish wandb run
wandb.finish()
