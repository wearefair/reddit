const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const Dotenv = require('dotenv-webpack');

const SRC_DIR = path.resolve(__dirname, 'src/');
const BUILD_DIR = path.resolve(__dirname, 'build/');

const HtmlWebpackPluginConfig = new HtmlWebpackPlugin({
  template: `${SRC_DIR}/index.html`,
  filename: 'index.html',
  inject: 'body',
});

const DotEnvPlugin = new Dotenv({
  path: path.resolve(__dirname, '.env'), // Path to .env file (this is the default)
  safe: true, // load .env.example (defaults to "false" which does not use dotenv-safe)
});

module.exports = {
  devtool: 'source-maps',
  context: SRC_DIR,
  entry: ['./index.js'],
  output: {
    filename: '[name].bundle.js',
    chunkFilename: '[id].bundle.js',
    path: BUILD_DIR,
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)?$/,
        enforce: 'pre',
        include: [
          SRC_DIR,
        ],
        exclude: /\.*test.js/,
        loader: 'eslint-loader',
      },
      {
        test: /\.(js|jsx)?$/,
        include: SRC_DIR,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: ['env', 'flow', 'react', 'es2017', 'stage-2'],
              plugins: ['syntax-flow'],
            },
          },
        ],
      },
      {
        test: /\.less$/,
        use: [
          {
            loader: 'style-loader',
          },
          {
            loader: 'css-loader',
          },
          {
            loader: 'less-loader',
          },
        ],
      },
      {
        test: /\.[ot]tf$/,
        loader: 'url-loader',
        options: {
          limit: 65000,
          mimetype: 'application/octet-stream',
          prefix: path.resolve(SRC_DIR, 'fonts/'),
        },
      },
    ],
  },
  plugins: [HtmlWebpackPluginConfig, DotEnvPlugin],
  devServer: {
    historyApiFallback: true
  },
};