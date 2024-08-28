// /static/js/scripts.js

import { handleSwaggerFileChange } from './swagger-handler.js';
import { handleFilterFileChange } from './filter-handler.js';
import { handleFilterFormSubmit, handleDownloadFilter } from './form-handler.js';

document.getElementById('filter').addEventListener('change', handleFilterFileChange);

document.getElementById('swagger').addEventListener('change', handleSwaggerFileChange);

document.getElementById('filter-form').addEventListener('submit', handleFilterFormSubmit);

document.getElementById('download-filter').addEventListener('click', handleDownloadFilter);
