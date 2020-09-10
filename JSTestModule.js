const assert = require('assert').strict;


module.exports = function (filePath, solution) {
    require(filePath).forEach(({ input, output }) => {
        assert.deepEqual(solution(...input), output);
    });
};
