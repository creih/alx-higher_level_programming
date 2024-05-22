#!/usr/bin/node
// displaying usrs bafite completed field iri true
const request = require('request');
const inzira = process.argv[2];
request(inzira, (error, response, body) => {
if (error) {
  console.error('Error:', error);
} else if (response.statusCode !== 200) {
  console.log(`Error: ${response.statusCode}`);
} else {
  const t = JSON.parse(body);
  const comp = {};
  t.forEach(task => {
    if (task.completed) {
      if (!comp[task.userId]) {
        comp[task.userId] = 0;
      }
      comp[task.userId]++;
    }
  });
  sorti = '{ ';
  for (const userId in comp) {
    if (comp.hasOwnProperty(userId)) {
      sorti += `\'${userId}\': ${comp[userId]},\n`;
    }
  }
  sorti = sorti.slice(0, -2); 
  sorti += ' }';
	console.log(sorti);
}
});
