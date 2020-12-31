

default_search_space_dict = dict()



xgboost_regressor_search_space = {'learning_rate_multiplier': [(0.5, 10), 'real', 'uniform'],
										 'gamma': [(0, 5), 'real', 'uniform'],
										 'max_depth': [(2, 20), 'discrete'],
										 'n_estimators': [(10, 1250), 'discrete'],
										 'min_child_weight': [(1, 50), 'discrete'],
										 'colsample_bytree': [(0.1, 1), 'real', 'uniform'],
										 'subsample': [(0.1, 1), 'real', 'uniform'],
										 'reg_alpha': [(0, 1), 'real', 'loguniform'],
										 'reg_lambda': [(1, 5), 'real', 'loguniform']}

xgboost_regressor_search_space_str = \
"""
{'learning_rate_multiplier': [(0.5, 10), 'real', 'uniform'],
 'gamma': [(0, 5), 'real', 'uniform'],
 'max_depth': [(2, 20), 'discrete'],
 'n_estimators': [(10, 1250), 'discrete'],
 'min_child_weight': [(1, 50), 'discrete'],
 'colsample_bytree': [(0.1, 1), 'real', 'uniform'],
 'subsample': [(0.1, 1), 'real', 'uniform'],
 'reg_alpha': [(0, 1), 'real', 'loguniform'],
 'reg_lambda': [(1, 5), 'real', 'loguniform']}"""

default_search_space_dict['xgboost_regressor'] = [xgboost_regressor_search_space, xgboost_regressor_search_space_str]


tiny_xgboost_regressor_search_space = {'learning_rate_multiplier': [(0.5, 10), 'real', 'uniform'],
										 'gamma': [(0, 5), 'real', 'uniform'],
										 'max_depth': [(2, 3), 'discrete'],
										 'n_estimators': [(10, 25), 'discrete'],
										 'min_child_weight': [(1, 50), 'discrete'],
										 'colsample_bytree': [(0.1, 1), 'real', 'uniform'],
										 'subsample': [(0.1, 1), 'real', 'uniform'],
										 'reg_alpha': [(0, 1), 'real', 'loguniform'],
										 'reg_lambda': [(1, 5), 'real', 'loguniform']}

tiny_xgboost_regressor_search_space_str = \
"""
{'learning_rate_multiplier': [(0.5, 10), 'real', 'uniform'],
 'gamma': [(0, 5), 'real', 'uniform'],
 'max_depth': [(2, 3), 'discrete'],
 'n_estimators': [(10, 25), 'discrete'],
 'min_child_weight': [(1, 50), 'discrete'],
 'colsample_bytree': [(0.1, 1), 'real', 'uniform'],
 'subsample': [(0.1, 1), 'real', 'uniform'],
 'reg_alpha': [(0, 1), 'real', 'loguniform'],
 'reg_lambda': [(1, 5), 'real', 'loguniform']}"""

default_search_space_dict['tiny_xgboost_regressor'] = [tiny_xgboost_regressor_search_space, tiny_xgboost_regressor_search_space_str]


