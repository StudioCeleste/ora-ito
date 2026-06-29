module.exports = function(eleventyConfig) {
  eleventyConfig.addGlobalData("permalink", () => {
    return (data) => {
      // Avoid changing permalink for html files that are just passed through or custom permalinks
      if (data.permalink) return data.permalink;
      return `${data.page.filePathStem}.html`;
    };
  });
  
  // Also passthrough assets
  eleventyConfig.addPassthroughCopy("src/assets");

  return {
    dir: {
      input: "src",
      output: "_site"
    }
  };
};
