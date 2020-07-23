function solution(T) {
    const depth = tree => {
        if (!tree)
            return 0;
        return Math.max(depth(tree.l), depth(tree.r)) + 1;
    };
    return Math.max(depth(T.l), depth(T.r))
}