// Set the correct URL for the API
export function setApiUrl(localUrl: string) {
  const environments = {
    development: "http://localhost:8000/api",
    // development: "https://backend.dktshumen.com/api",
    // production: "http://localhost:8000/api",
    production: "https://backend.dktshumen.com/api",
  };

  const apiUrl = environments[process.env.NODE_ENV] || environments.production;

  return `${apiUrl}${localUrl}`;
}

// Set the correct URL for images
export function setThumborUrl(localUrl: string, imgOptions: string) {
  const thumborUrl = "https://images.dktshumen.com";
  // const thumborUrl = "http://127.0.0.1:8001";
  const prodUrl = "https://www.dktshumen.com/";
  // const prodUrl = "http://127.0.0.1:3000";

  return `${thumborUrl}/?img_url=${prodUrl}${localUrl}&options=${imgOptions}`;
}
