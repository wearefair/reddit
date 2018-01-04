// Set default node environment to development
process.env.NODE_ENV = process.env.NODE_ENV || 'development';
const path = require('path');
const express = require('express');

const port = process.env.OPENSHIFT_NODEJS_PORT ||
           process.env.PORT ||
           9000;
const ip = process.env.OPENSHIFT_NODEJS_IP ||
           process.env.IP ||
           9000;

const app = express();

app.use(express.static('./build'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build/index.html'));
});

// Start server
app.listen(port, ip, () => {
  console.log('Express server listening on %d, in %s mode', port, app.get('env'));
});
