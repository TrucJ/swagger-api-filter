// /static/js/form-handler.js

import { appState } from './scripts.js';

export function handleFilterFormSubmit(event) {
    event.preventDefault();
    const swaggerFileInput = document.getElementById('swagger');

    if (!swaggerFileInput.files.length) {
        alert('Please upload the Swagger file.');
        return;
    }

    if (!appState.filterData) {
        alert('No updated filter data available.');
        return;
    }

    const formData = new FormData();
    formData.append('swagger', swaggerFileInput.files[0]);

    const filterBlob = new Blob([JSON.stringify(appState.filterData, null, 2)], { type: 'application/json' });
    formData.append('filter', filterBlob, 'updated_filter.json');

    fetch('/filter/beauty', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        const outputFileName = generateOutputFileName(swaggerFileInput.files[0].name);
        downloadFile(JSON.stringify(data, null, 2), outputFileName);
    })
    .catch(error => console.error('Error:', error));
}

export function handleDownloadFilter(event) {
    if (!appState.filterData) {
        alert('No filter data available for download.');
        return;
    }

    const filterJson = JSON.stringify(appState.filterData, null, 2);
    const filterFileName = 'updated_filter.json';
    downloadFile(filterJson, filterFileName);
}

export function updateFilterData(event) {
    const [method, path] = event.target.id.split('-');
    const isChecked = event.target.checked;

    if (!appState.filterData.paths[path]) {
        appState.filterData.paths[path] = [];
    }

    if (isChecked) {
        if (!appState.filterData.paths[path].includes(method)) {
            appState.filterData.paths[path].push(method);
        }
    } else {
        const index = appState.filterData.paths[path].indexOf(method);
        if (index > -1) {
            appState.filterData.paths[path].splice(index, 1);
        }

        if (appState.filterData.paths[path].length === 0) {
            delete appState.filterData.paths[path];
        }
    }
}

function generateOutputFileName(originalFileName) {
    const swaggerFileNameParts = originalFileName.split('.');
    swaggerFileNameParts[0] += '_filter';
    return swaggerFileNameParts.join('.');
}

function downloadFile(content, fileName) {
    const blob = new Blob([content], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = fileName;
    link.click();
}
