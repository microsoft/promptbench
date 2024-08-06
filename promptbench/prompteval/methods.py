import copy
import numpy as np
from sklearn.linear_model import LogisticRegression as LR  # type: ignore
from tqdm import tqdm  # type: ignore
try: from .utils import check_multicolinearity
except ImportError: from utils import check_multicolinearity

class LogisticRegression:
    """
    Logistic regression model.

    Attributes:
        reg (float): The regularization parameter for the logistic regression model. This is equivalent to the prior Gaussian covariance scaling in the Bayesian setup with gaussian, ie, prior cov = reg*identity.
    """

    def __init__(self, reg=1e2):
        """
        Initializes the logistic regression model with a regularization parameter.

        Parameters:
            reg (float): Regularization parameter (default is 100).
        """
        self.reg = reg

    def fit(self, X, y):
        """
        Fits the logistic regression model to the data.

        Parameters:
            X (array-like): Feature matrix.
            y (array-like): Target vector of 0s and 1s.
        """
        # This block of code is just a trick to run the Scikit-Learn implementation for logistic regression
        if np.var(y) == 0:
            y_copy = copy.deepcopy(y)
            local_state = np.random.RandomState(0)
            ind = local_state.choice(len(y_copy))
            y_copy[ind] = 1 - np.median(y_copy)
        else:
            y_copy = copy.deepcopy(y)

        # Fitting the model
        logreg = LR(C=self.reg, random_state=0, solver="liblinear", fit_intercept=False).fit(X, y_copy)
        self.mu = logreg.coef_.squeeze()


class ExtendedRaschModel:
    """
    An extended Rasch model incorporating covariates for both formats and examples.

    Attributes:
        seen_examples (array-like): Boolean array indicating seen examples.
        Y (array-like): Target matrix of 0s and 1s.
        X (array-like): Covariates for formats.
        Z (array-like): Covariates for examples.
        x_dim (int): Dimension of X.
        z_dim (int): Dimension of Z.
        n_formats (int): Number of formats.
        n_examples (int): Number of examples.
        rasch_model (LogisticRegression): The fitted logistic regression model.
        gammas (array-like): Coefficients for the format covariates.
        thetas (array-like): Format parameters.
        psi (array-like): Coefficients for the example covariates.
        betas (array-like): Example parameters.
        logits (array-like): Logits of the fitted model.
    """

    def __init__(self):
        """
        Initializes the extended Rasch model.
        """
        pass

    def fit(self, seen_examples, Y, X=None, Z=None):
        """
        Fits the extended Rasch model to the data.

        Parameters:
            seen_examples (array-like): Boolean array indicating seen examples.
            Y (array-like): Target matrix.
            X (array-like): Covariates for formats (default is identity matrix).
            Z (array-like): Covariates for examples (default is identity matrix).
        """
        self.seen_examples = seen_examples
        self.Y = Y

        # X (formats covariates)
        if type(X) != np.ndarray:
            self.X = np.eye(Y.shape[0])
        else:
            self.X = X
            check_multicolinearity(X)
        self.x_dim = self.X.shape[1]

        # Z (examples covariates)
        if type(Z) != np.ndarray:
            self.Z = np.eye(Y.shape[1])
        else:
            self.Z = Z
            check_multicolinearity(Z)
        self.z_dim = self.Z.shape[1]

        # Formatting the data
        self.n_formats, self.n_examples = seen_examples.shape
        features, labels = GenXY(seen_examples, Y, self.X, self.Z)

        if type(X) != np.ndarray and type(Z) != np.ndarray:  # basic Rasch model (no need to include intercept)
            features = features[:, :-1]
        elif (
            type(X) != np.ndarray or type(Z) != np.ndarray
        ):  # just one set of covariates (no need to include intercept)
            pass
        else:  # two sets of covariates (need to include intercept)
            features = np.hstack((features, np.ones((features.shape[0], 1))))

        # Fitting the model
        self.rasch_model = LogisticRegression()
        self.rasch_model.fit(features, labels)

        # Predicted probs
        self.gammas = self.rasch_model.mu[: self.x_dim]
        self.thetas = self.X @ self.gammas
        self.psi = self.rasch_model.mu[self.x_dim :]

        if type(X) != np.ndarray and type(Z) != np.ndarray:  # basic Rasch model (no intercept)
            self.betas = np.hstack((self.psi, np.array([0])))
            self.logits = self.thetas[:, None] + self.betas[None, :]
        elif type(X) != np.ndarray or type(Z) != np.ndarray:  # just one set of covariates (no intercept)
            self.betas = self.Z @ self.psi
            self.logits = self.thetas[:, None] + self.betas[None, :]
        else:  # two sets of covariates (intercept included)
            self.betas = self.Z @ self.psi[:-1]
            self.logits = self.thetas[:, None] + self.betas[None, :] + self.psi[-1]

    def get_Y_hat(self):
        """
        Computes the predicted probabilities.

        Returns:
            array-like: Predicted probabilities.
        """
        P_hat = sigmoid(self.logits)
        Y_hat = np.zeros(self.seen_examples.shape)
        Y_hat[self.seen_examples] = self.Y[self.seen_examples]
        Y_hat[~self.seen_examples] = P_hat[~self.seen_examples]
        return Y_hat


class LogReg:
    """
    A logistic regression model tailored for the Rasch model.

    Attributes:
        X (array-like): Covariates for formats.
        Z (array-like): Covariates for examples.
        x_dim (int): Dimension of X.
        z_dim (int): Dimension of Z.
        n_formats (int): Number of formats.
        n_examples (int): Number of examples.
        rasch_model (LogisticRegression): The fitted logistic regression model.
        gammas (array-like): Coefficients for the format covariates.
        thetas (array-like): Format parameters.
        logits (array-like): Logits of the fitted model.
        seen_examples (array-like): Boolean array indicating seen examples.
        Y (array-like): Target matrix.
    """

    def __init__(self):
        """
        Initializes the logistic regression model.
        """
        pass

    def fit(self, seen_items, Y, X=None):
        """
        Fits the logistic regression model to the data.

        Parameters:
            seen_items (array-like): Boolean array indicating seen items.
            Y (array-like): Target matrix.
            X (array-like): Covariates for formats (default is identity matrix).
        """

        # X (formats covariates)
        if type(X) != np.ndarray:
            self.X = np.eye(Y.shape[0])
        else:
            self.X = X
        self.x_dim = self.X.shape[1]

        # Z (examples covariates)
        self.Z = np.eye(Y.shape[1])
        self.z_dim = self.Z.shape[1]

        # Formatting the data
        self.n_formats, self.n_examples = seen_items.shape
        features, labels = GenXY(seen_items, Y, self.X, self.Z)
        features = features[:, : self.x_dim]
        if type(X) == np.ndarray:  # assuming LI columns
            features = np.hstack((features, np.ones((features.shape[0], 1))))

        # Fitting the model
        self.rasch_model = LogisticRegression()
        self.rasch_model.fit(features, labels)

        # Predicted probs
        self.gammas = self.rasch_model.mu[: self.x_dim]
        self.thetas = self.X @ self.gammas
        self.logits = self.thetas[:, None] + self.rasch_model.mu[-1] + np.zeros(Y.shape)
        self.seen_examples = seen_items
        self.Y = Y

    def get_Y_hat(self):
        """
        Computes the predicted probabilities.

        Returns:
            array-like: Predicted probabilities.
        """
        P_hat = sigmoid(self.logits)
        Y_hat = np.zeros(self.seen_examples.shape)
        Y_hat[self.seen_examples] = self.Y[self.seen_examples]
        Y_hat[~self.seen_examples] = P_hat[~self.seen_examples]
        return Y_hat


class PromptEval:
    """
    A class for evaluating prompts using logistic regression or extended Rasch models.

    Attributes:
        seen_examples (array-like): Boolean array indicating seen examples.
        quantiles (list): List of quantiles for evaluation.
        estimates (dict): Dictionary to store evaluation metrics.
    """

    def __init__(self):
        """
        Initializes the prompt evaluation.
        """
        pass

    def fit(self, Y, quantiles, rounds_eval, X=None, Z=None, logreg=False, random_seed=None, verbose=False):
        """
        Fits the model and evaluates the prompts.

        Parameters:
            Y (array-like): Target matrix.
            quantiles (list): List of quantiles for evaluation.
            rounds_eval (list): List of evaluation rounds.
            X (array-like): Covariates for formats (default is None).
            Z (array-like): Covariates for examples (default is None).
            logreg (bool): Flag to use logistic regression (default is False).
            random_seed (int): Random seed for reproducibility (default is None).
            verbose (bool): Flag to enable verbose output (default is False).
        """
        n_formats, n_examples = Y.shape
        self.seen_examples = np.zeros(Y.shape).astype(bool)
        self.quantiles = quantiles
        self.estimates = {"n_seen": [], "pirt": [], "accs_hat": []}

        for num_seen_examples in tqdm(rounds_eval, disable=not verbose):
            # sampling
            self.seen_examples = StratSample(self.seen_examples, num_seen_examples, random_seed)

            # fit model
            if logreg:
                self.rasch_model = LogReg()
                self.rasch_model.fit(self.seen_examples, Y, X)
            else:
                self.rasch_model = ExtendedRaschModel()
                self.rasch_model.fit(self.seen_examples, Y, X, Z)
            self.estimates["n_seen"].append(self.seen_examples.sum())

            # pIRT
            quants_hat = np.percentile(self.rasch_model.get_Y_hat().mean(-1), quantiles)
            self.estimates["pirt"].append(quants_hat.tolist())

            # accs_hat
            self.estimates["accs_hat"].append(self.rasch_model.get_Y_hat().mean(-1).tolist())


class Baseline:
    """
    A baseline model for evaluating prompts.

    Attributes:
        seen_examples (array-like): Boolean array indicating seen examples.
        quantiles (list): List of quantiles for evaluation.
        estimates (dict): Dictionary to store evaluation metrics.
    """

    def __init__(self):
        """
        Initializes the baseline model.
        """
        pass

    def fit(self, Y, quantiles, rounds_eval, random_seed=None):
        """
        Fits the baseline model and evaluates the prompts.

        Parameters:
            Y (array-like): Target matrix.
            quantiles (list): List of quantiles for evaluation.
            rounds_eval (list): List of evaluation rounds.
            random_seed (int): Random seed for reproducibility (default is None).
        """
        n_formats, n_examples = Y.shape
        self.seen_examples = np.zeros(Y.shape).astype(bool)
        self.quantiles = quantiles
        self.estimates = {"n_seen": [], "estimates": [], "accs_hat": []}

        for num_seen_examples in rounds_eval:
            self.seen_examples = StratSample(self.seen_examples, num_seen_examples, random_seed)
            eps = 1e-10
            accs = np.array([(Y[i, s].sum() + eps) / (s.sum() + eps) for i, s in enumerate(self.seen_examples)])
            self.estimates["n_seen"].append(self.seen_examples.sum())
            self.estimates["estimates"].append(np.percentile(accs, quantiles).tolist())
            self.estimates["accs_hat"].append(accs.tolist())


def StratSample(seen_examples, max_seen, random_seed, active_arms=None, random_column=False):
    """
    Generates a stratified sample from the seen examples matrix until the maximum number of seen examples is reached.

    Parameters:
    seen_examples (array-like): The matrix of seen examples.
    max_seen (int): The maximum number of seen examples.
    random_seed (int): The random seed for reproducibility.
    active_arms (list or ndarray, optional): List of active arms. Defaults to None.
    random_column (bool, optional): If True, selects a column randomly. Defaults to False.

    Returns:
    array-like: The updated matrix of seen examples.
    """
    matrix = seen_examples
    rows, columns = matrix.shape

    if type(active_arms) == list or type(active_arms) == np.ndarray:
        pass
    else:
        active_arms = list(range(rows))

    current_ones = np.sum(matrix)  # noqa
    local_state = np.random.RandomState(random_seed)

    while True:
        if np.sum(matrix) >= max_seen:
            return matrix

        next_row = local_state.choice(
            [
                i
                for i in range(len(active_arms))
                if (matrix[active_arms].sum(1) == np.min(matrix[active_arms].sum(1)))[i]
            ]
        )
        next_row = active_arms[next_row]
        avail_columns = [i for i in range(matrix.shape[1]) if matrix[next_row, i] == False]

        if avail_columns == []:  # nothing else to see
            return matrix

        if random_column:
            next_column = local_state.choice(avail_columns)
        else:
            next_columns = [i for i in avail_columns if matrix[:, i].sum() == matrix[:, avail_columns].sum(0).min()]
            next_column = local_state.choice(next_columns)

        matrix[next_row, next_column] = True


def GenXY(seen_items, Y, X, Z):
    """
    Generates combined feature and label matrices.

    Parameters:
    seen_items (array-like): Matrix indicating which items have been seen.
    Y (array-like): Target values matrix.
    X (array-like): Feature matrix for the first set of features.
    Z (array-like): Feature matrix for the second set of features.

    Returns:
    tuple: Combined feature matrix and corresponding labels.
    """
    Y_seen = -np.ones(Y.shape)
    Y_seen[seen_items] = Y[seen_items]

    W_x = []
    W_z = []

    labels = []
    for i in range(seen_items.shape[0]):
        for j in range(seen_items.shape[1]):
            if seen_items[i, j] == True:
                W_x.append(X[i])
                W_z.append(Z[j])
                labels.append(Y_seen[i, j])

    W = np.hstack((np.vstack(W_x), np.vstack(W_z)))
    labels = np.array(labels)
    return W, labels


def sigmoid(x):
    """
    Applies the sigmoid function to the input.

    Parameters:
    x (array-like): The input data.

    Returns:
    array-like: The output of the sigmoid function.
    """
    x_clipped = np.clip(x, -30, 30)
    return 1 / (1 + np.exp(-x_clipped))
