#!/usr/bin/env node
/**
 * AI Tools Index Data Updater
 * Run: node scripts/update-data.js
 * 
 * This script helps maintain the AI tools database.
 * For production, integrate with APIs for real-time data.
 */

const fs = require('fs');
const path = require('path');

// Data file path
const DATA_FILE = path.join(__dirname, '../data/tools.json');

// Load existing data
function loadData() {
  try {
    return JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
  } catch (e) {
    return { tools: [], lastUpdated: null };
  }
}

// Save data
function saveData(data) {
  data.lastUpdated = new Date().toISOString();
  data.totalTools = data.tools.length;
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
  console.log(`Saved ${data.tools.length} tools`);
}

// Update a specific tool
function updateTool(data, name, updates) {
  const tool = data.tools.find(t => t.name.toLowerCase() === name.toLowerCase());
  if (tool) {
    Object.assign(tool, updates);
    console.log(`Updated: ${name}`);
  } else {
    console.log(`Not found: ${name}`);
  }
}

// Add a new tool
function addTool(data, tool) {
  const existing = data.tools.find(t => t.name.toLowerCase() === tool.name.toLowerCase());
  if (existing) {
    Object.assign(existing, tool);
    console.log(`Updated existing: ${tool.name}`);
  } else {
    tool.id = data.tools.length + 1;
    tool.ranking = tool.ranking || data.tools.length + 1;
    data.tools.push(tool);
    console.log(`Added: ${tool.name}`);
  }
}

// Main
const data = loadData();

// Example: Update Craftit with accurate data
updateTool(data, 'Craftit', {
  social: {
    instagram: 1700,
    twitter: 200,
    tiktok: 100,
    facebook: 300
  },
  estimatedUsers: 5000,
  estimatedMonthlyVisits: 15000
});

saveData(data);
console.log('Data update complete!');
