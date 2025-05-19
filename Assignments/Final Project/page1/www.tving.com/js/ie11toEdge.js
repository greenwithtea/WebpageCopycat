if (/MSIE \d|Trident.*rv:/.test(navigator.userAgent)) {
    /* eslint-disable */
    window.location = 'microsoft-edge:' + window.location;
    setTimeout(function () {
        window.location = 'https://go.microsoft.com/fwlink/?linkid=2135547';
    }, 1);
}
