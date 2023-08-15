#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const values = Object.values(dict);
const uniqueValues = [...new Set(values)];
const newDictionary = {};
for (const j in uniqueValues) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === uniqueValues[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDictionary[uniqueValues[j]] = list;
}
console.log(newDictionary);
