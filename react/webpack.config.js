const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");

const proxy = { '/api': {
                        target: 'http://localhost:8000',
                        //pathRewrite: {"^/api": ""},
                    },
                };

module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.join(__dirname, "../eda/templates"),
        filename: "bundle.js"
    },
    devServer: { 
            proxy : proxy,
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html"
        })
    ]
}