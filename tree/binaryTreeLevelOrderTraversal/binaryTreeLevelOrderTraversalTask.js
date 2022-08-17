class node {
    constructor(value, left, right) {
        this.left = left;
        this.right = right;
        this.value = value;
    }
}

const preorderTraversal = (root, valueList = []) => {
    if (root != null) {
        valueList.push(root.value);
        preorderTraversal(root.left, valueList);
        preorderTraversal(root.right, valueList);
    }
    return valueList;
}

const getLevel = (root, level, levelNodesList = []) => {
    if (root == null) {
        return [];
    }
    if (level == 1) {
        levelNodesList.push(root.value)
    }
    else {
        getLevel(root.left, level - 1, levelNodesList);
        getLevel(root.right, level - 1, levelNodesList);
    }
    return levelNodesList;
}

const levelOrder = (root, valueList = []) => {
    first_level = []
    first_level = getLevel(root, 1, [])
    if (first_level.length == 0) {
        return first_level;
    }
    else {
        valueList.push(first_level);
    }
    let i = 2;
    while (true) {
        levelNodesList = []
        getLevel(root, i, levelNodesList);
        if (levelNodesList.length == 0) {
            break;
        }
        else {
            valueList.push(levelNodesList);
        }
        i += 1;
    }
    return valueList;
}

valueList = [];
root = new node(1, new node(2, new node(3, null, null), new node(4, new node(5, null, null), new node(6, null, null))), new node(7, null, null))
root = null
console.log(levelOrder(root, valueList))