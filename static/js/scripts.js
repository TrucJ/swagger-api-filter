// /static/js/scripts.js

import { handleSwaggerFileChange } from './swagger-handler.js';
import { handleFilterFileChange, autoCheckPaths } from './filter-handler.js';
import { handleFilterFormSubmit, handleDownloadFilter } from './form-handler.js';

export const appState = {
    swaggerFile: null,
    filterData: {"paths": {}},
};

document.getElementById('filter').addEventListener('change', handleFilterFileChange);

document.getElementById('swagger').addEventListener('change', handleSwaggerFileChange);

document.getElementById('filter-form').addEventListener('submit', handleFilterFormSubmit);

document.getElementById('download-filter').addEventListener('click', handleDownloadFilter);
