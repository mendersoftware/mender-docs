var retext = require('retext');
var engine = require('unified-engine');

engine(
  {
    // Standard engine configuration
    processor: retext,
    files: ['.'],
    extensions: ['md', 'markdown', 'mkd', 'mkdn', 'mkdown'],
    pluginPrefix: 'retext',
    packageField: 'retextConfig',
    color: true
  },
  (error, failed) => {
    if (error || failed === 1) throw error;
  }
);
