const path = require('path')
const webpack = require('webpack')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const ESLintPlugin = require('eslint-webpack-plugin')

const entries = {

}

const projectRoot = process.env.PWD || process.cwd()

module.exports = {
    resolve: {
        symlinks: false
    },
    entry: entries,
    output: {
        clean: {
            keep: /sprites/
        },
        filename: '[name].js',
        path: path.resolve(projectRoot, './project/static/dist')
    },
    module: {
        rules: [
            {
                test: /\.m?js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                        targets: "defaults",
                        plugins: ['@babel/plugin-proposal-optional-chaining']
                    }
                }
            },
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader',
                        options: {
                            sourceMap: true,
                        },
                    },
                    {
                        loader: "postcss-loader",
                        options: {
                            postcssOptions: {
                                config: path.resolve(projectRoot, './project/static/build/postcss.config.js'),
                            }
                        },
                    },
                ],
            },
        ]
    },
    plugins: [
        new ESLintPlugin({
            files: ['./project/static/src/**/*.js'],
        }),
        new MiniCssExtractPlugin({
            filename: '[name].css',
        }),
        new webpack.DefinePlugin({
            'process.env.BUILD': JSON.stringify('web'),
        }),
    ]
}
