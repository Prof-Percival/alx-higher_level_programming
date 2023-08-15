#!/usr/bin/node
const datalist = require('./100-data.js').list;
console.log(datalist);
console.log(datalist.map((item, index) => item * index));
