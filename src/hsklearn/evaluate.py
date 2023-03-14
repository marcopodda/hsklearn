import hydra
from omegaconf import DictConfig


def evaluate(cfg: DictConfig):
    """Evaluate function."""
    print(cfg)


@hydra.main(
    version_base="1.3",
    config_path="../../config",
    config_name="evaluate.yaml",
)
def main(cfg: DictConfig) -> None:
    """Main function."""
    evaluate(cfg)


if __name__ == "__main__":
    # pylint:disable=no-value-for-parameter
    main()
