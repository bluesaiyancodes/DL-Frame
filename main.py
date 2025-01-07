# main.py
import hydra
from omegaconf import DictConfig, OmegaConf
import logging

import src.utils.conutils as utils 


@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig):
    # check log printing
    if cfg.other.log_print:
        console_handler = utils.log_printer()
        logging.getLogger().addHandler(console_handler)

    # Obtain a module-level logger
    logger = logging.getLogger(__name__)

    print(f"Selected Dataset - {cfg.dataset.name}, see the config/log file for more details.")
    # log the configuration
    logger.info("Experiment Configuration:\n%s", OmegaConf.to_yaml(cfg))  
    hydra_cfg = hydra.core.hydra_config.HydraConfig.get()
    out_dir = hydra_cfg['runtime']['output_dir']
    print(f"Experiment output directory: {out_dir}")
    
    

if __name__ == "__main__":
    main()
