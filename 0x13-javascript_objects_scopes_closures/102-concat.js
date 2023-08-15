#!/usr/bin/node
const fs = require('fs');
const fileRead1 = fs.readFileSync(process.argv[2], 'utf8');
const fileRead2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], fileRead1 + fileRead2);
