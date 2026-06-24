module.exports = function(eleventyConfig) {
  // Passthrough copy for assets and CMS admin
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/admin");

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      layouts: "_includes",
      data: "_data"
    },
    templateFormats: ["html", "njk", "md", "liquid"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk"
  };
};
