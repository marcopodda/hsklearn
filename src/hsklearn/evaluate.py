import hydra
from omegaconf import DictConfig

from hsklearn import CONFIG_ROOT


def evaluate(cfg: DictConfig):
    """Evaluate function."""
    print(cfg)


@hydra.main(
    version_base="1.3",
    config_path=CONFIG_ROOT.as_posix(),
    config_name="evaluate.yaml",
)
def main(cfg: DictConfig) -> None:
    """Main function."""
    evaluate(cfg)


if __name__ == "__main__":
    # pylint:disable=no-value-for-parameter
    main()
