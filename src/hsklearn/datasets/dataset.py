import numpy as np
import pandas as pd


class Dataset:
    """A class to wrap a ML dataset."""

    def __init__(
        self,
        features: pd.DataFrame,
        targets: pd.Series,
        train_idx: np.ndarray,
        test_idx: np.ndarray,
    ):
        self.features = features
        self.targets = targets
        self.train_idx = train_idx
        self.test_idx = test_idx

    @property
    def X_train(self) -> pd.DataFrame:
        """Returns the training set."""
        return self.features.loc[self.train_idx]

    @property
    def X_test(self) -> pd.DataFrame:
        """Returns the test set."""
        return self.features.loc[self.test_idx]

    @property
    def y_train(self) -> pd.Series:
        """Returns the training targets."""
        return self.targets.loc[self.train_idx]

    @property
    def y_test(self) -> pd.Series:
        """Returns the test targets."""
        return self.targets.loc[self.test_idx]
