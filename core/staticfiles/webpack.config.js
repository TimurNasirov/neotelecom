const path = require('path');
const _modules = {
  index: './src/index.js',
  main: './src/main.js',
  map: './src/map.js',
  join_us: './src/join-us.js',
  tariffs: './src/tariffs.js',
  channels: './src/channels.js',
  handbook: './src/handbook.js',
};
const WebpackMd5Hash = require('webpack-md5-hash');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CleanWebpackPlugin = require('clean-webpack-plugin');
const ImageminPlugin = require('imagemin-webpack-plugin').default;
const CopyWebpackPlugin = require('copy-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
module.exports = {
  entry: _modules,
  output: {
    path: path.resolve(__dirname, 'dst'),
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        // exclude: [/(node_modules|js-libs)/],
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.(scss|css)$/,
        use: ['style-loader', MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader', 'sass-loader']
      },
      {
        test: /\.(jpg|png|svg|gif)$/,
        loader: 'file-loader',
        options: {
          name: 'img/[name].[ext]'
        }
      },
      {
        test: /\.(woff)$/,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[ext]'
        }
      },
    ]
  },
  plugins: [
    new CleanWebpackPlugin('dst', {}),
    new UglifyJsPlugin({
      cache: true,
      parallel: true,
      uglifyOptions: {
        compress: true,
        ecma: 5,
        mangle: true
      },
      sourceMap: false
    }),
    new MiniCssExtractPlugin({
      filename: 'index.css',
    }),
    // new HtmlWebpackPlugin({
    //   inject: false,
    //   hash: true,
    //   template: './src/index.html',
    //   filename: '../../templates/layout.html'
    // }),
    new WebpackMd5Hash(),
    new ImageminPlugin({ test: /\.(jpe?g|png|gif|svg)$/i }),
    new CopyWebpackPlugin([
      { from: 'src/img/', to: 'img' }
    ])
  ]
};