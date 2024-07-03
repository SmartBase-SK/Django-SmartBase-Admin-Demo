module.exports = {
    root: true,
    env: {
        browser: true,
        es2021: true,
    },
    extends: [
        'airbnb-base',
    ],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
    },
    rules: {
        indent: ['error', 4],
        semi: ['error', 'never'], 'class-methods-use-this': 0,
        'no-new': 0,
        'new-cap': 0,
        'max-len': ['error', { 'code': 120, 'tabWidth': 4 }],
        'no-param-reassign': ['error', {'props': false}]
    },
};
