import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # 生成索引
    indices = np.arange(n_samples)

    # 随机打乱
    if shuffle:
        np.random.shuffle(indices)

    # 取测试集和实验集
    base_size = n_samples // k
    test = n_samples % k

    fold_size = []
    for i in range(k):
        if i < test:
            fold_size.append(base_size + 1)
        else:
            fold_size.append(base_size)

    # 切分K折
    folds = []
    start = 0
    for size in fold_size:
        fold = indices[start: start + size]
        folds.append(fold)
        start = start + size
    
    # K折交叉验证，每折轮流当测试集
    result = []
    for i in range(k):
        test_indices = folds[i]        # 第i折当测试集
        
        train_indices = []      # 训练集是其余的所有折
        for j in range(k):
            if j != i:
                train_indices.append(folds[j])
        train = np.concatenate(train_indices)   # 合并训练集
        
        result.append((train.tolist(), test_indices.tolist()))

    return result


