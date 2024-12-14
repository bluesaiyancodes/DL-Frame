# main.py
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig):
    # Print the entire configuration
    print("Configuration:\n", OmegaConf.to_yaml(cfg))

    # Access specific configurations
    print("Model name:", cfg.model.name)
    print("Pretrained:", cfg.model.pretrained)
    print("Training epochs:", cfg.training.epochs)
    print("Dataset name:", cfg.dataset.name)

    # Here you would typically instantiate your model, dataset, and training loop based on the config:
    # Example (pseudocode):
    # model = build_model(cfg.model.name, pretrained=cfg.model.pretrained)
    # train_loader, val_loader = get_dataloaders(cfg.dataset.root, cfg.training.batch_size)
    # trainer = Trainer(epochs=cfg.training.epochs, lr=cfg.training.learning_rate)
    # trainer.train(model, train_loader, val_loader)

if __name__ == "__main__":
    main()
