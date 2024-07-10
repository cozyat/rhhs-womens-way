(function () {
	function VerticalTimeline(element) {
		this.element = element;
		this.blocks = this.element.getElementsByClassName("cd-timeline__block");
		this.images = this.element.getElementsByClassName("cd-timeline__img");
		this.contents = this.element.getElementsByClassName("cd-timeline__content");
		this.offset = 0.8;
		this.hideBlocks();
	};

	VerticalTimeline.prototype.hideBlocks = function () {
		if (!"classList" in document.documentElement) {
			return; // no animation on older browsers
		}
		var self = this;
		for (var i = 0; i < this.blocks.length; i++) {
			(function (i) {
				if (self.blocks[i].getBoundingClientRect().top > window.innerHeight * self.offset) {
					self.images[i].classList.add("cd-timeline__img--hidden");
					self.contents[i].classList.add("cd-timeline__content--hidden");
				}
			})(i);
		}
	};

	VerticalTimeline.prototype.showBlocks = function () {
		if (!"classList" in document.documentElement) {
			return;
		}
		var self = this;
		for (var i = 0; i < this.blocks.length; i++) {JiyaJI
			(function (i) {
				if (self.contents[i].classList.contains("cd-timeline__content--hidden") && self.blocks[i].getBoundingClientRect().top <= window.innerHeight * self.offset) {
					self.images[i].classList.add("cd-timeline__img--bounce-in");
					self.contents[i].classList.add("cd-timeline__content--bounce-in");
					self.images[i].classList.remove("cd-timeline__img--hidden");
					self.contents[i].classList.remove("cd-timeline__content--hidden");
				}
			})(i);
		}
	};

	var verticalTimelines = document.getElementsByClassName("js-cd-timeline"),
		verticalTimelinesArray = [],
		scrolling = false;
	if (verticalTimelines.length > 0) {
		for (var i = 0; i < verticalTimelines.length; i++) {
			(function (i) {
				verticalTimelinesArray.push(new VerticalTimeline(verticalTimelines[i]));
			})(i);
		}
		window.addEventListener("scroll", function (event) {
			if (!scrolling) {
				scrolling = true;
				(!window.requestAnimationFrame) ? setTimeout(checkTimelineScroll, 250) : window.requestAnimationFrame(checkTimelineScroll);
			}
		});
	}

	function checkTimelineScroll() {
		verticalTimelinesArray.forEach(function (timeline) {
			timeline.showBlocks();
		});
		scrolling = false;
	};
})();

window.onload = function () {
	function checkResolution() {
		var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
		var height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
		var section = document.getElementById("responsive-image-section");
		var hr = document.querySelector("hr.landing");
		var messageContainer = document.getElementById("resolution-message");

		if (width < 1200 || height < 800) {
			if (section) {
				section.style.display = "none";
			}
			if (hr) {
				hr.style.display = "none";
			}
			if (messageContainer) {
				messageContainer.innerHTML = "We are sorry but the Women's Way Team Profile Picture cannot be displayed on your device.";
				messageContainer.style.fontFamily = "'Arial', sans-serif";
				messageContainer.style.fontSize = "20px";
				messageContainer.style.fontWeight = "bold";
				messageContainer.style.animation = "flash 1s infinite";
				messageContainer.style.display = "block";
			}
		} else {
			if (section) {
				section.style.display = "block";
			}
			if (hr) {
				hr.style.display = "block";
			}
			if (messageContainer) {
				messageContainer.innerHTML = '';
				messageContainer.style.display = "none";
			}
		}
	}

	window.onresize = function () {
		checkResolution();
	};

	checkResolution();
};