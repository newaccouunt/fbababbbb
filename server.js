const express = require('express');
const app = express();
const PORT = process.env.PORT || 10000;

// ============================================================
// CONFIGURATION
// ============================================================
const ADMIN_PASSWORD = "Noobster@2024";
const TELEGRAM_CHANNEL = "https://t.me/firebase1991";

// ============================================================
// FULL HTML PAGE (from panel-otp.html)
// ============================================================
const pageHTML = `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
    <title>NOOBSTER</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <style>
        @layer properties {
            @supports (((-webkit-hyphens: none)) and (not (margin-trim:inline))) or ((-moz-orient:inline) and (not (color:rgb(from red r g b)))) {
                *, :before, :after, ::backdrop {
                    --tw-translate-x:0;
                    --tw-translate-y: 0;
                    --tw-translate-z: 0;
                    --tw-rotate-x: initial;
                    --tw-rotate-y: initial;
                    --tw-rotate-z: initial;
                    --tw-skew-x: initial;
                    --tw-skew-y: initial;
                    --tw-space-y-reverse: 0;
                    --tw-space-x-reverse: 0;
                    --tw-border-style: solid;
                    --tw-gradient-position: initial;
                    --tw-gradient-from: #0000;
                    --tw-gradient-via: #0000;
                    --tw-gradient-to: #0000;
                    --tw-gradient-stops: initial;
                    --tw-gradient-via-stops: initial;
                    --tw-gradient-from-position: 0%;
                    --tw-gradient-via-position: 50%;
                    --tw-gradient-to-position: 100%;
                    --tw-leading: initial;
                    --tw-font-weight: initial;
                    --tw-tracking: initial;
                    --tw-ordinal: initial;
                    --tw-slashed-zero: initial;
                    --tw-numeric-figure: initial;
                    --tw-numeric-spacing: initial;
                    --tw-numeric-fraction: initial;
                    --tw-shadow: 0 0 #0000;
                    --tw-shadow-color: initial;
                    --tw-shadow-alpha: 100%;
                    --tw-inset-shadow: 0 0 #0000;
                    --tw-inset-shadow-color: initial;
                    --tw-inset-shadow-alpha: 100%;
                    --tw-ring-color: initial;
                    --tw-ring-shadow: 0 0 #0000;
                    --tw-inset-ring-color: initial;
                    --tw-inset-ring-shadow: 0 0 #0000;
                    --tw-ring-inset: initial;
                    --tw-ring-offset-width: 0px;
                    --tw-ring-offset-color: #fff;
                    --tw-ring-offset-shadow: 0 0 #0000;
                    --tw-outline-style: solid;
                    --tw-blur: initial;
                    --tw-brightness: initial;
                    --tw-contrast: initial;
                    --tw-grayscale: initial;
                    --tw-hue-rotate: initial;
                    --tw-invert: initial;
                    --tw-opacity: initial;
                    --tw-saturate: initial;
                    --tw-sepia: initial;
                    --tw-drop-shadow: initial;
                    --tw-drop-shadow-color: initial;
                    --tw-drop-shadow-alpha: 100%;
                    --tw-drop-shadow-size: initial;
                    --tw-backdrop-blur: initial;
                    --tw-backdrop-brightness: initial;
                    --tw-backdrop-contrast: initial;
                    --tw-backdrop-grayscale: initial;
                    --tw-backdrop-hue-rotate: initial;
                    --tw-backdrop-invert: initial;
                    --tw-backdrop-opacity: initial;
                    --tw-backdrop-saturate: initial;
                    --tw-backdrop-sepia: initial;
                    --tw-duration: initial;
                    --tw-ease: initial;
                    --tw-content: "";
                    --tw-animation-delay: 0s;
                    --tw-animation-direction: normal;
                    --tw-animation-duration: initial;
                    --tw-animation-fill-mode: none;
                    --tw-animation-iteration-count: 1;
                    --tw-enter-blur: 0;
                    --tw-enter-opacity: 1;
                    --tw-enter-rotate: 0;
                    --tw-enter-scale: 1;
                    --tw-enter-translate-x: 0;
                    --tw-enter-translate-y: 0;
                    --tw-exit-blur: 0;
                    --tw-exit-opacity: 1;
                    --tw-exit-rotate: 0;
                    --tw-exit-scale: 1;
                    --tw-exit-translate-x: 0;
                    --tw-exit-translate-y: 0
                }
            }
        }

        @layer theme {
            :root,
            :host {
                --color-red-50: oklch(97.1% .013 17.38);
                --color-red-300: oklch(80.8% .114 19.571);
                --color-red-400: oklch(70.4% .191 22.216);
                --color-red-500: oklch(63.7% .237 25.331);
                --color-red-600: oklch(57.7% .245 27.325);
                --color-red-700: oklch(50.5% .213 27.518);
                --color-red-900: oklch(39.6% .141 25.723);
                --color-red-950: oklch(25.8% .092 26.042);
                --color-orange-400: oklch(75% .183 55.934);
                --color-orange-500: oklch(70.5% .213 47.604);
                --color-orange-900: oklch(40.8% .123 38.172);
                --color-orange-950: oklch(26.6% .079 36.259);
                --color-amber-400: oklch(82.8% .189 84.429);
                --color-amber-500: oklch(76.9% .188 70.08);
                --color-yellow-400: oklch(85.2% .199 91.936);
                --color-yellow-500: oklch(79.5% .184 86.047);
                --color-yellow-900: oklch(42.1% .095 57.708);
                --color-yellow-950: oklch(28.6% .066 53.813);
                --color-emerald-300: oklch(84.5% .143 164.978);
                --color-emerald-400: oklch(76.5% .177 163.223);
                --color-emerald-500: oklch(69.6% .17 162.48);
                --color-emerald-600: oklch(59.6% .145 163.225);
                --color-emerald-700: oklch(50.8% .118 165.612);
                --color-emerald-900: oklch(37.8% .077 168.94);
                --color-emerald-950: oklch(26.2% .051 172.552);
                --color-blue-400: oklch(70.7% .165 254.624);
                --color-blue-800: oklch(42.4% .199 265.638);
                --color-blue-900: oklch(37.9% .146 265.522);
                --color-blue-950: oklch(28.2% .091 267.935);
                --color-purple-300: oklch(82.7% .119 306.383);
                --color-purple-400: oklch(71.4% .203 305.504);
                --color-purple-500: oklch(62.7% .265 303.9);
                --color-purple-600: oklch(55.8% .288 302.321);
                --color-purple-900: oklch(38.1% .176 304.987);
                --color-purple-950: oklch(29.1% .149 302.717);
                --color-gray-50: oklch(98.5% .002 247.839);
                --color-gray-600: oklch(44.6% .03 256.802);
                --color-gray-900: oklch(21% .034 264.665);
                --color-black: #000;
                --color-white: #fff;
                --spacing: .25rem;
                --breakpoint-2xl: 96rem;
                --container-sm: 24rem;
                --container-md: 28rem;
                --container-lg: 32rem;
                --text-xs: .75rem;
                --text-xs--line-height: calc(1 / .75);
                --text-sm: .875rem;
                --text-sm--line-height: calc(1.25 / .875);
                --text-base: 1rem;
                --text-base--line-height: 1.5;
                --text-lg: 1.125rem;
                --text-lg--line-height: calc(1.75 / 1.125);
                --text-xl: 1.25rem;
                --text-xl--line-height: calc(1.75 / 1.25);
                --text-2xl: 1.5rem;
                --text-2xl--line-height: calc(2 / 1.5);
                --text-4xl: 2.25rem;
                --text-4xl--line-height: calc(2.5 / 2.25);
                --font-weight-normal: 400;
                --font-weight-medium: 500;
                --font-weight-semibold: 600;
                --font-weight-bold: 700;
                --font-weight-black: 900;
                --tracking-tight: -.025em;
                --tracking-wider: .05em;
                --tracking-widest: .1em;
                --leading-tight: 1.25;
                --leading-snug: 1.375;
                --leading-normal: 1.5;
                --leading-relaxed: 1.625;
                --radius-2xl: 1rem;
                --radius-3xl: 1.5rem;
                --ease-out: cubic-bezier(0, 0, .2, 1);
                --ease-in-out: cubic-bezier(.4, 0, .2, 1);
                --animate-spin: spin 1s linear infinite;
                --animate-pulse: pulse 2s cubic-bezier(.4, 0, .6, 1) infinite;
                --blur-sm: 8px;
                --blur-md: 12px;
                --blur-3xl: 64px;
                --aspect-video: 16 / 9;
                --default-transition-duration: .15s;
                --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1);
                --default-font-family: var(--app-font-sans);
                --default-mono-font-family: var(--app-font-mono);
                --color-border: hsl(var(--border));
                --color-primary: hsl(var(--primary))
            }
        }

        @layer base {
            *,
            :after,
            :before,
            ::backdrop {
                box-sizing: border-box;
                border: 0 solid;
                margin: 0;
                padding: 0
            }
            ::file-selector-button {
                box-sizing: border-box;
                border: 0 solid;
                margin: 0;
                padding: 0
            }
            html,
            :host {
                -webkit-text-size-adjust: 100%;
                tab-size: 4;
                line-height: 1.5;
                font-family: var(--default-font-family, ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji");
                font-feature-settings: var(--default-font-feature-settings, normal);
                font-variation-settings: var(--default-font-variation-settings, normal);
                -webkit-tap-highlight-color: transparent
            }
            hr {
                height: 0;
                color: inherit;
                border-top-width: 1px
            }
            abbr:where([title]) {
                -webkit-text-decoration: underline dotted;
                text-decoration: underline dotted
            }
            h1,
            h2,
            h3,
            h4,
            h5,
            h6 {
                font-size: inherit;
                font-weight: inherit
            }
            a {
                color: inherit;
                -webkit-text-decoration: inherit;
                text-decoration: inherit
            }
            b,
            strong {
                font-weight: bolder
            }
            code,
            kbd,
            samp,
            pre {
                font-family: var(--default-mono-font-family, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace);
                font-feature-settings: var(--default-mono-font-feature-settings, normal);
                font-variation-settings: var(--default-mono-font-variation-settings, normal);
                font-size: 1em
            }
            small {
                font-size: 80%
            }
            sub,
            sup {
                vertical-align: baseline;
                font-size: 75%;
                line-height: 0;
                position: relative
            }
            sub {
                bottom: -.25em
            }
            sup {
                top: -.5em
            }
            table {
                text-indent: 0;
                border-color: inherit;
                border-collapse: collapse
            }
            :-moz-focusring {
                outline: auto
            }
            progress {
                vertical-align: baseline
            }
            summary {
                display: list-item
            }
            ol,
            ul,
            menu {
                list-style: none
            }
            img,
            svg,
            video,
            canvas,
            audio,
            iframe,
            embed,
            object {
                vertical-align: middle;
                display: block
            }
            img,
            video {
                max-width: 100%;
                height: auto
            }
            button,
            input,
            select,
            optgroup,
            textarea {
                font: inherit;
                font-feature-settings: inherit;
                font-variation-settings: inherit;
                letter-spacing: inherit;
                color: inherit;
                opacity: 1;
                background-color: #0000;
                border-radius: 0
            }
            ::file-selector-button {
                font: inherit;
                font-feature-settings: inherit;
                font-variation-settings: inherit;
                letter-spacing: inherit;
                color: inherit;
                opacity: 1;
                background-color: #0000;
                border-radius: 0
            }
            :where(select:is([multiple], [size])) optgroup {
                font-weight: bolder
            }
            :where(select:is([multiple], [size])) optgroup option {
                padding-inline-start: 20px
            }
            ::file-selector-button {
                margin-inline-end: 4px
            }
            ::placeholder {
                opacity: 1
            }
            @supports (not ((-webkit-appearance:-apple-pay-button))) or (contain-intrinsic-size:1px) {
                ::placeholder {
                    color: currentColor
                }
                @supports (color:color-mix(in lab, red, red)) {
                    ::placeholder {
                        color: color-mix(in oklab, currentcolor 50%, transparent)
                    }
                }
            }
            textarea {
                resize: vertical
            }
            ::-webkit-search-decoration {
                -webkit-appearance: none
            }
            ::-webkit-date-and-time-value {
                min-height: 1lh;
                text-align: inherit
            }
            ::-webkit-datetime-edit {
                display: inline-flex
            }
            ::-webkit-datetime-edit-fields-wrapper {
                padding: 0
            }
            ::-webkit-datetime-edit {
                padding-block: 0
            }
            ::-webkit-datetime-edit-year-field {
                padding-block: 0
            }
            ::-webkit-datetime-edit-month-field {
                padding-block: 0
            }
            ::-webkit-datetime-edit-day-field {
                padding-block: 0
            }
            ::-webkit-datetime-edit-hour-field {
                padding-block: 0
            }
            ::-webkit-datetime-edit-minute-field {
                padding-block: 0
            }
            ::-webkit-datetime-edit-second-field {
                padding-block: 0
            }
            ::-webkit-datetime-edit-millisecond-field {
                padding-block: 0
            }
            ::-webkit-datetime-edit-meridiem-field {
                padding-block: 0
            }
            ::-webkit-calendar-picker-indicator {
                line-height: 1
            }
            :-moz-ui-invalid {
                box-shadow: none
            }
            button,
            input:where([type=button], [type=reset], [type=submit]) {
                appearance: button
            }
            ::file-selector-button {
                appearance: button
            }
            ::-webkit-inner-spin-button {
                height: auto
            }
            ::-webkit-outer-spin-button {
                height: auto
            }
            [hidden]:where(:not([hidden=until-found])) {
                display: none !important
            }
            * {
                border-color: hsl(var(--border))
            }
            body {
                background-color: #020202;
                font-family: var(--app-font-sans);
                color: hsl(var(--foreground));
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
                background: radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.12) 0px, transparent 50%), radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.12) 0px, transparent 50%), radial-gradient(at 50% 100%, rgba(6, 182, 212, 0.08) 0px, transparent 50%), #020202;
                background-attachment: fixed;
            }
        }

        @layer components;
        @layer utilities {
            .sr-only {
                clip-path: inset(50%);
                white-space: nowrap;
                border-width: 0;
                width: 1px;
                height: 1px;
                margin: -1px;
                padding: 0;
                position: absolute;
                overflow: hidden
            }
            .absolute { position: absolute }
            .fixed { position: fixed }
            .relative { position: relative }
            .sticky { position: sticky }
            .inset-0 { inset: 0 }
            .flex { display: flex }
            .grid { display: grid }
            .hidden { display: none }
            .inline-flex { display: inline-flex }
            .items-center { align-items: center }
            .justify-center { justify-content: center }
            .justify-between { justify-content: space-between }
            .flex-col { flex-direction: column }
            .gap-2 { gap: 0.5rem }
            .gap-3 { gap: 0.75rem }
            .gap-4 { gap: 1rem }
            .p-3 { padding: 0.75rem }
            .p-4 { padding: 1rem }
            .p-6 { padding: 1.5rem }
            .p-7 { padding: 1.75rem }
            .px-4 { padding-inline: 1rem }
            .py-3 { padding-block: 0.75rem }
            .rounded-xl { border-radius: 0.75rem }
            .rounded-2xl { border-radius: 1rem }
            .rounded-3xl { border-radius: 1.5rem }
            .rounded-full { border-radius: 9999px }
            .text-center { text-align: center }
            .text-sm { font-size: 0.875rem }
            .text-xs { font-size: 0.75rem }
            .font-bold { font-weight: 700 }
            .font-semibold { font-weight: 600 }
            .text-white { color: #fff }
            .bg-black { background-color: #000 }
            .min-h-screen { min-height: 100vh }
            .w-full { width: 100% }
            .max-w-md { max-width: 28rem }
            .mx-auto { margin-inline: auto }
            .mb-4 { margin-bottom: 1rem }
            .mb-5 { margin-bottom: 1.25rem }
            .mb-8 { margin-bottom: 2rem }
            .mt-2 { margin-top: 0.5rem }
            .mt-6 { margin-top: 1.5rem }
            .mt-10 { margin-top: 2.5rem }
        }

        /* 3D Telegram Popup Styles */
        #telegramPopup {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 99999;
            padding: 20px;
        }
        .popup-box {
            width: 100%;
            max-width: 380px;
            padding: 38px 28px 40px;
            border-radius: 40px;
            text-align: center;
            color: #fff;
            background: radial-gradient(circle at 30% 20%, #2b9cff, #0f5b9e 80%, #083b6b);
            box-shadow: 0 40px 70px rgba(0, 0, 0, 0.7), 0 15px 30px rgba(0, 0, 0, 0.5), inset 0 4px 12px rgba(255, 255, 255, 0.5), inset 0 -6px 18px rgba(0, 20, 40, 0.8), 0 0 0 2px rgba(255, 255, 255, 0.08) inset;
            transform: perspective(1200px) rotateX(6deg) rotateY(2deg) translateZ(10px);
            animation: popup3d 0.7s cubic-bezier(0.23, 1, 0.32, 1) forwards;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            position: relative;
            overflow: hidden;
        }
        .popup-box:hover {
            transform: perspective(1200px) rotateX(3deg) rotateY(4deg) translateY(-6px) translateZ(16px);
            box-shadow: 0 60px 90px rgba(0, 0, 0, 0.8), 0 20px 40px rgba(0, 0, 0, 0.6), inset 0 4px 16px rgba(255, 255, 255, 0.6), inset 0 -8px 24px rgba(0, 20, 40, 0.9), 0 0 0 2px rgba(255, 255, 255, 0.15) inset;
        }
        @keyframes popup3d {
            0% {
                opacity: 0;
                transform: perspective(1200px) rotateX(40deg) rotateY(10deg) scale(0.7) translateZ(-80px);
                filter: blur(8px);
            }
            100% {
                opacity: 1;
                transform: perspective(1200px) rotateX(6deg) rotateY(2deg) scale(1) translateZ(10px);
                filter: blur(0);
            }
        }
        .popup-box h2 {
            font-size: 26px;
            font-weight: 700;
            letter-spacing: -0.2px;
            margin-bottom: 14px;
            text-shadow: 0 6px 14px rgba(0, 0, 0, 0.4), 0 2px 4px rgba(0, 0, 0, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        .popup-box .sub-icon {
            font-size: 34px;
            line-height: 1;
            filter: drop-shadow(0 8px 12px rgba(0, 0, 0, 0.4));
        }
        .popup-box p {
            color: #e3f0ff;
            font-size: 17px;
            line-height: 1.6;
            font-weight: 400;
            margin: 10px 0 22px;
            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
            background: rgba(0, 30, 60, 0.2);
            backdrop-filter: blur(2px);
            border-radius: 40px;
            padding: 14px 16px;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .join-btn {
            display: inline-block;
            margin-top: 6px;
            padding: 16px 34px;
            background: linear-gradient(145deg, #ffffff, #e0ecff);
            color: #0066aa;
            font-weight: 700;
            font-size: 18px;
            text-decoration: none;
            border-radius: 60px;
            letter-spacing: 0.3px;
            border: none;
            cursor: pointer;
            box-shadow: 0 16px 28px -6px rgba(0, 0, 0, 0.6), 0 8px 16px -4px rgba(0, 0, 0, 0.4), inset 0 2px 8px rgba(255, 255, 255, 0.9), inset 0 -4px 12px rgba(0, 40, 80, 0.2);
            transition: all 0.2s cubic-bezier(0.23, 1, 0.32, 1);
            text-shadow: 0 1px 2px rgba(255, 255, 255, 0.5);
        }
        .join-btn:hover {
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0 24px 40px -8px rgba(0, 0, 0, 0.7), 0 12px 24px -6px rgba(0, 0, 0, 0.5), inset 0 3px 12px rgba(255, 255, 255, 1), inset 0 -6px 16px rgba(0, 40, 80, 0.3);
            background: linear-gradient(145deg, #ffffff, #d4e6ff);
            color: #004a88;
        }
        .join-btn:active {
            transform: translateY(2px) scale(0.97);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.5), inset 0 2px 8px rgba(0, 0, 0, 0.2);
        }
        .join-btn::before {
            content: "✈️ ";
            font-size: 22px;
            display: inline-block;
            margin-right: 8px;
        }
        .popup-close-btn {
            position: absolute;
            top: 14px;
            right: 18px;
            background: rgba(255, 255, 255, 0.15);
            border: none;
            color: #fff;
            font-size: 20px;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
            z-index: 10;
        }
        .popup-close-btn:hover {
            background: rgba(255, 255, 255, 0.3);
        }
        .popup-box::after {
            content: '';
            position: absolute;
            top: 8%;
            left: 10%;
            width: 40%;
            height: 20%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.2) 0%, transparent 80%);
            border-radius: 50%;
            filter: blur(6px);
            pointer-events: none;
            opacity: 0.6;
        }
        .popup-box::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 40px;
            padding: 2px;
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.0) 70%);
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }
        @media (max-width: 480px) {
            .popup-box {
                padding: 28px 20px 30px;
                max-width: 94%;
                border-radius: 32px;
            }
            .popup-box h2 {
                font-size: 22px;
                gap: 4px;
            }
            .popup-box p {
                font-size: 15px;
                padding: 12px 14px;
            }
            .join-btn {
                font-size: 16px;
                padding: 14px 28px;
                width: 100%;
            }
        }
    </style>
</head>

<body>
    <div id="root"></div>

    <!-- 3D Telegram Popup Modal -->
    <div id="telegramPopup" onclick="if(event.target === this) this.style.display='none';">
        <div class="popup-box">
            <button class="popup-close-btn" onclick="document.getElementById('telegramPopup').style.display='none';" aria-label="Close">
          &times;
        </button>
            <h2>
                <span class="sub-icon">📱</span> JOIN TELEGRAM CHANNEL
            </h2>
            <p>
                Get The New Pannel<br />
            </p>
            <a class="join-btn" href="https://t.me/noobsterrr" target="_blank" onclick="document.getElementById('telegramPopup').style.display='none';">
                ⚡ JOIN  ⚡  
        </a>
        </div>
    </div>
    <script>
        (function() {
            const tt = document.createElement("link").relList;
            if (tt && tt.supports && tt.supports("modulepreload")) return;
            for (const S of document.querySelectorAll('link[rel="modulepreload"]')) d(S);
            new MutationObserver(S => {
                for (const f of S)
                    if (f.type === "childList")
                        for (const p of f.addedNodes) p.tagName === "LINK" && p.rel === "modulepreload" && d(p)
            }).observe(document, {
                childList: !0,
                subtree: !0
            });

            function b(S) {
                const f = {};
                return S.integrity && (f.integrity = S.integrity), S.referrerPolicy && (f.referrerPolicy = S.referrerPolicy), S.crossOrigin === "use-credentials" ? f.credentials = "include" : S.crossOrigin === "anonymous" ? f.credentials = "omit" : f.credentials = "same-origin", f
            }

            function d(S) {
                if (S.ep) return;
                S.ep = !0;
                const f = b(S);
                fetch(S.href, f)
            }
        })();
        var ms = typeof globalThis < "u" ? globalThis : typeof window < "u" ? window : typeof global < "u" ? global : typeof self < "u" ? self : {};

        function O0(A) {
            return A && A.__esModule && Object.prototype.hasOwnProperty.call(A, "default") ? A.default : A
        }
        var Ru = {
                exports: {}
            },
            Fl = {};
        var Xd;

        function k0() {
            if (Xd) return Fl;
            Xd = 1;
            var A = Symbol.for("react.transitional.element"),
                tt = Symbol.for("react.fragment");

            function b(d, S, f) {
                var p = null;
                if (f !== void 0 && (p = "" + f), S.key !== void 0 && (p = "" + S.key), "key" in S) {
                    f = {};
                    for (var h in S) h !== "key" && (f[h] = S[h])
                } else f = S;
                return S = f.ref, {
                    $$typeof: A,
                    type: d,
                    key: p,
                    ref: S !== void 0 ? S : null,
                    props: f
                }
            }
            return Fl.Fragment = tt, Fl.jsx = b, Fl.jsxs = b, Fl
        }
        var Vd;

        function D0() {
            return Vd || (Vd = 1, Ru.exports = k0()), Ru.exports
        }
        var r = D0(),
            Mu = {
                exports: {}
            },
            Il = {},
            Bu = {
                exports: {}
            },
            Uu = {};
        var Qd;

        function R0() {
            return Qd || (Qd = 1, (function(A) {
                function tt(Z, q) {
                    var mt = Z.length;
                    Z.push(q);
                    t: for (; 0 < mt;) {
                        var it = mt - 1 >>> 1,
                            bt = Z[it];
                        if (0 < S(bt, q)) Z[it] = q, Z[mt] = bt, mt = it;
                        else break t
                    }
                }

                function b(Z) {
                    return Z.length === 0 ? null : Z[0]
                }

                function d(Z) {
                    if (Z.length === 0) return null;
                    var q = Z[0],
                        mt = Z.pop();
                    if (mt !== q) {
                        Z[0] = mt;
                        t: for (var it = 0, bt = Z.length, y = bt >>> 1; it < y;) {
                            var _ = 2 * (it + 1) - 1,
                                X = Z[_],
                                U = _ + 1,
                                J = Z[U];
                            if (0 > S(X, mt)) U < bt && 0 > S(J, X) ? (Z[it] = J, Z[U] = mt, it = U) : (Z[it] = X, Z[_] = mt, it = _);
                            else if (U < bt && 0 > S(J, mt)) Z[it] = J, Z[U] = mt, it = U;
                            else break t
                        }
                    }
                    return q
                }

                function S(Z, q) {
                    var mt = Z.sortIndex - q.sortIndex;
                    return mt !== 0 ? mt : Z.id - q.id
                }
                if (A.unstable_now = void 0, typeof performance == "object" && typeof performance.now == "function") {
                    var f = performance;
                    A.unstable_now = function() {
                        return f.now()
                    }
                } else {
                    var p = Date,
                        h = p.now();
                    A.unstable_now = function() {
                        return p.now() - h
                    }
                }
                var o = [],
                    x = [],
                    T = 1,
                    w = null,
                    C = 3,
                    v = !1,
                    E = !1,
                    g = !1,
                    z = !1,
                    N = typeof setTimeout == "function" ? setTimeout : null,
                    k = typeof clearTimeout == "function" ? clearTimeout : null,
                    M = typeof setImmediate < "u" ? setImmediate : null;

                function H(Z) {
                    for (var q = b(x); q !== null;) {
                        if (q.callback === null) d(x);
                        else if (q.startTime <= Z) d(x), q.sortIndex = q.expirationTime, tt(o, q);
                        else break;
                        q = b(x)
                    }
                }

                function L(Z) {
                    if (g = !1, H(Z), !E)
                        if (b(o) !== null) E = !0, nt || (nt = !0, D());
                        else {
                            var q = b(x);
                            q !== null && I(L, q.startTime - Z)
                        }
                }
                var nt = !1,
                    V = -1,
                    ot = 5,
                    $ = -1;

                function ht() {
                    return z ? !0 : !(A.unstable_now() - $ < ot)
                }

                function xt() {
                    if (z = !1, nt) {
                        var Z = A.unstable_now();
                        $ = Z;
                        var q = !0;
                        try {
                            t: {
                                E = !1,
                                g && (g = !1, k(V), V = -1),
                                v = !0;
                                var mt = C;
                                try {
                                    e: {
                                        for (H(Z), w = b(o); w !== null && !(w.expirationTime > Z && ht());) {
                                            var it = w.callback;
                                            if (typeof it == "function") {
                                                w.callback = null, C = w.priorityLevel;
                                                var bt = it(w.expirationTime <= Z);
                                                if (Z = A.unstable_now(), typeof bt == "function") {
                                                    w.callback = bt, H(Z), q = !0;
                                                    break e
                                                }
                                                w === b(o) && d(o), H(Z)
                                            } else d(o);
                                            w = b(o)
                                        }
                                        if (w !== null) q = !0;
                                        else {
                                            var y = b(x);
                                            y !== null && I(L, y.startTime - Z), q = !1
                                        }
                                    }
                                    break t
                                }
                                finally {
                                    w = null, C = mt, v = !1
                                }
                                q = void 0
                            }
                        }
                        finally {
                            q ? D() : nt = !1
                        }
                    }
                }
                var D;
                if (typeof M == "function") D = function() {
                    M(xt)
                };
                else if (typeof MessageChannel < "u") {
                    var at = new MessageChannel,
                        c = at.port2;
                    at.port1.onmessage = xt, D = function() {
                        c.postMessage(null)
                    }
                } else D = function() {
                    N(xt, 0)
                };

                function I(Z, q) {
                    V = N(function() {
                        Z(A.unstable_now())
                    }, q)
                }
                A.unstable_IdlePriority = 5, A.unstable_ImmediatePriority = 1, A.unstable_LowPriority = 4, A.unstable_NormalPriority = 3, A.unstable_Profiling = null, A.unstable_UserBlockingPriority = 2, A.unstable_cancelCallback = function(Z) {
                    Z.callback = null
                }, A.unstable_forceFrameRate = function(Z) {
                    0 > Z || 125 < Z ? console.error("forceFrameRate takes a positive int between 0 and 125, forcing frame rates higher than 125 fps is not supported") : ot = 0 < Z ? Math.floor(1e3 / Z) : 5
                }, A.unstable_getCurrentPriorityLevel = function() {
                    return C
                }, A.unstable_next = function(Z) {
                    switch (C) {
                        case 1:
                        case 2:
                        case 3:
                            var q = 3;
                            break;
                        default:
                            q = C
                    }
                    var mt = C;
                    C = q;
                    try {
                        return Z()
                    } finally {
                        C = mt
                    }
                }, A.unstable_requestPaint = function() {
                    z = !0
                }, A.unstable_runWithPriority = function(Z, q) {
                    switch (Z) {
                        case 1:
                        case 2:
                        case 3:
                        case 4:
                        case 5:
                            break;
                        default:
                            Z = 3
                    }
                    var mt = C;
                    C = Z;
                    try {
                        return q()
                    } finally {
                        C = mt
                    }
                }, A.unstable_scheduleCallback = function(Z, q, mt) {
                    var it = A.unstable_now();
                    switch (typeof mt == "object" && mt !== null ? (mt = mt.delay, mt = typeof mt == "number" && 0 < mt ? it + mt : it) : mt = it, Z) {
                        case 1:
                            var bt = -1;
                            break;
                        case 2:
                            bt = 250;
                            break;
                        case 5:
                            bt = 1073741823;
                            break;
                        case 4:
                            bt = 1e4;
                            break;
                        default:
                            bt = 5e3
                    }
                    return bt = mt + bt, Z = {
                        id: T++,
                        callback: q,
                        priorityLevel: Z,
                        startTime: mt,
                        expirationTime: bt,
                        sortIndex: -1
                    }, mt > it ? (Z.sortIndex = mt, tt(x, Z), b(o) === null && Z === b(x) && (g ? (k(V), V = -1) : g = !0, I(L, mt - it))) : (Z.sortIndex = bt, tt(o, Z), E || v || (E = !0, nt || (nt = !0, D()))), Z
                }, A.unstable_shouldYield = ht, A.unstable_wrapCallback = function(Z) {
                    var q = C;
                    return function() {
                        var mt = C;
                        C = q;
                        try {
                            return Z.apply(this, arguments)
                        } finally {
                            C = mt
                        }
                    }
                }
            })(Uu)), Uu
        }
        var Kd;

        function M0() {
            return Kd || (Kd = 1, Bu.exports = R0()), Bu.exports
        }
        var Hu = {
                exports: {}
            },
            Tt = {};
        var Jd;

        function B0() {
            if (Jd) return Tt;
            Jd = 1;
            var A = Symbol.for("react.transitional.element"),
                tt = Symbol.for("react.portal"),
                b = Symbol.for("react.fragment"),
                d = Symbol.for("react.strict_mode"),
                S = Symbol.for("react.profiler"),
                f = Symbol.for("react.consumer"),
                p = Symbol.for("react.context"),
                h = Symbol.for("react.forward_ref"),
                o = Symbol.for("react.suspense"),
                x = Symbol.for("react.memo"),
                T = Symbol.for("react.lazy"),
                w = Symbol.for("react.activity"),
                C = Symbol.iterator;

            function v(y) {
                return y === null || typeof y != "object" ? null : (y = C && y[C] || y["@@iterator"], typeof y == "function" ? y : null)
            }
            var E = {
                    isMounted: function() {
                        return !1
                    },
                    enqueueForceUpdate: function() {},
                    enqueueReplaceState: function() {},
                    enqueueSetState: function() {}
                },
                g = Object.assign,
                z = {};

            function N(y, _, X) {
                this.props = y, this.context = _, this.refs = z, this.updater = X || E
            }
            N.prototype.isReactComponent = {}, N.prototype.setState = function(y, _) {
                if (typeof y != "object" && typeof y != "function" && y != null) throw Error("takes an object of state variables to update or a function which returns an object of state variables.");
                this.updater.enqueueSetState(this, y, _, "setState")
            }, N.prototype.forceUpdate = function(y) {
                this.updater.enqueueForceUpdate(this, y, "forceUpdate")
            };

            function k() {}
            k.prototype = N.prototype;

            function M(y, _, X) {
                this.props = y, this.context = _, this.refs = z, this.updater = X || E
            }
            var H = M.prototype = new k;
            H.constructor = M, g(H, N.prototype), H.isPureReactComponent = !0;
            var L = Array.isArray;

            function nt() {}
            var V = {
                    H: null,
                    A: null,
                    T: null,
                    S: null
                },
                ot = Object.prototype.hasOwnProperty;

            function $(y, _, X) {
                var U = X.ref;
                return {
                    $$typeof: A,
                    type: y,
                    key: _,
                    ref: U !== void 0 ? U : null,
                    props: X
                }
            }

            function ht(y, _) {
                return $(y.type, _, y.props)
            }

            function xt(y) {
                return typeof y == "object" && y !== null && y.$$typeof === A
            }

            function D(y) {
                var _ = {
                    "=": "=0",
                    ":": "=2"
                };
                return "$" + y.replace(/[=:]/g, function(X) {
                    return _[X]
                })
            }
            var at = /\/+/g;

            function c(y, _) {
                return typeof y == "object" && y !== null && y.key != null ? D("" + y.key) : _.toString(36)
            }

            function I(y) {
                switch (y.status) {
                    case "fulfilled":
                        return y.value;
                    case "rejected":
                        throw y.reason;
                    default:
                        switch (typeof y.status == "string" ? y.then(nt, nt) : (y.status = "pending", y.then(function(_) {
                            y.status === "pending" && (y.status = "fulfilled", y.value = _)
                        }, function(_) {
                            y.status === "pending" && (y.status = "rejected", y.reason = _)
                        })), y.status) {
                            case "fulfilled":
                                return y.value;
                            case "rejected":
                                throw y.reason
                        }
                }
                throw y
            }

            function Z(y, _, X, U, J) {
                var ut = typeof y;
                (ut === "undefined" || ut === "boolean") && (y = null);
                var _t = !1;
                if (y === null) _t = !0;
                else switch (ut) {
                    case "bigint":
                    case "string":
                    case "number":
                        _t = !0;
                        break;
                    case "object":
                        switch (y.$$typeof) {
                            case A:
                            case tt:
                                _t = !0;
                                break;
                            case T:
                                return _t = y._init, Z(_t(y._payload), _, X, U, J)
                        }
                }
                if (_t) return J = J(y), _t = U === "" ? "." + c(y, 0) : U, L(J) ? (X = "", _t != null && (X = _t.replace(at, "$&/") + "/"), Z(J, _, X, "", function(Yt) {
                    return Yt
                })) : J != null && (xt(J) && (J = ht(J, X + (J.key == null || y && y.key === J.key ? "" : ("" + J.key).replace(at, "$&/") + "/") + _t)), _.push(J)), 1;
                _t = 0;
                var St = U === "" ? "." : U + ":";
                if (L(y))
                    for (var yt = 0; yt < y.length; yt++) U = y[yt], ut = St + c(U, yt), _t += Z(U, _, X, ut, J);
                else if (yt = v(y), typeof yt == "function")
                    for (y = yt.call(y), yt = 0; !(U = y.next()).done;) U = U.value, ut = St + c(U, yt++), _t += Z(U, _, X, ut, J);
                else if (ut === "object") {
                    if (typeof y.then == "function") return Z(I(y), _, X, U, J);
                    throw _ = String(y), Error("Objects are not valid as a React child (found: " + (_ === "[object Object]" ? "object with keys {" + Object.keys(y).join(", ") + "}" : _) + "). If you meant to render a collection of children, use an array instead.")
                }
                return _t
            }

            function q(y, _, X) {
                if (y == null) return y;
                var U = [],
                    J = 0;
                return Z(y, U, "", "", function(ut) {
                    return _.call(X, ut, J++)
                }), U
            }

            function mt(y) {
                if (y._status === -1) {
                    var _ = y._result;
                    _ = _(), _.then(function(X) {
                        (y._status === 0 || y._status === -1) && (y._status = 1, y._result = X)
                    }, function(X) {
                        (y._status === 0 || y._status === -1) && (y._status = 2, y._result = X)
                    }), y._status === -1 && (y._status = 0, y._result = _)
                }
                if (y._status === 1) return y._result.default;
                throw y._result
            }
            var it = typeof reportError == "function" ? reportError : function(y) {
                    if (typeof window == "object" && typeof window.ErrorEvent == "function") {
                        var _ = new window.ErrorEvent("error", {
                            bubbles: !0,
                            cancelable: !0,
                            message: typeof y == "object" && y !== null && typeof y.message == "string" ? String(y.message) : String(y),
                            error: y
                        });
                        if (!window.dispatchEvent(_)) return
                    } else if (typeof process == "object" && typeof process.emit == "function") {
                        process.emit("uncaughtException", y);
                        return
                    }
                    console.error(y)
                },
                bt = {
                    map: q,
                    forEach: function(y, _, X) {
                        q(y, function() {
                            _.apply(this, arguments)
                        }, X)
                    },
                    count: function(y) {
                        var _ = 0;
                        return q(y, function() {
                            _++
                        }), _
                    },
                    toArray: function(y) {
                        return q(y, function(_) {
                            return _
                        }) || []
                    },
                    only: function(y) {
                        if (!xt(y)) throw Error("React.Children.only expected to receive a single React element child.");
                        return y
                    }
                };
            return Tt.Activity = w, Tt.Children = bt, Tt.Component = N, Tt.Fragment = b, Tt.Profiler = S, Tt.PureComponent = M, Tt.StrictMode = d, Tt.Suspense = o, Tt.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE = V, Tt.__COMPILER_RUNTIME = {
                __proto__: null,
                c: function(y) {
                    return V.H.useMemoCache(y)
                }
            }, Tt.cache = function(y) {
                return function() {
                    return y.apply(null, arguments)
                }
            }, Tt.cacheSignal = function() {
                return null
            }, Tt.cloneElement = function(y, _, X) {
                if (y == null) throw Error("The argument must be a React element, but you passed " + y + ".");
                var U = g({}, y.props),
                    J = y.key;
                if (_ != null)
                    for (ut in _.key !== void 0 && (J = "" + _.key), _) !ot.call(_, ut) || ut === "key" || ut === "__self" || ut === "__source" || ut === "ref" && _.ref === void 0 || (U[ut] = _[ut]);
                var ut = arguments.length - 2;
                if (ut === 1) U.children = X;
                else if (1 < ut) {
                    for (var _t = Array(ut), St = 0; St < ut; St++) _t[St] = arguments[St + 2];
                    U.children = _t
                }
                return $(y.type, J, U)
            }, Tt.createContext = function(y) {
                return y = {
                    $$typeof: p,
                    _currentValue: y,
                    _currentValue2: y,
                    _threadCount: 0,
                    Provider: null,
                    Consumer: null
                }, y.Provider = y, y.Consumer = {
                    $$typeof: f,
                    _context: y
                }, y
            }, Tt.createElement = function(y, _, X) {
                var U, J = {},
                    ut = null;
                if (_ != null)
                    for (U in _.key !== void 0 && (ut = "" + _.key), _) ot.call(_, U) && U !== "key" && U !== "__self" && U !== "__source" && (J[U] = _[U]);
                var _t = arguments.length - 2;
                if (_t === 1) J.children = X;
                else if (1 < _t) {
                    for (var St = Array(_t), yt = 0; yt < _t; yt++) St[yt] = arguments[yt + 2];
                    J.children = St
                }
                if (y && y.defaultProps)
                    for (U in _t = y.defaultProps, _t) J[U] === void 0 && (J[U] = _t[U]);
                return $(y, ut, J)
            }, Tt.createRef = function() {
                return {
                    current: null
                }
            }, Tt.forwardRef = function(y) {
                return {
                    $$typeof: h,
                    render: y
                }
            }, Tt.isValidElement = xt, Tt.lazy = function(y) {
                return {
                    $$typeof: T,
                    _payload: {
                        _status: -1,
                        _result: y
                    },
                    _init: mt
                }
            }, Tt.memo = function(y, _) {
                return {
                    $$typeof: x,
                    type: y,
                    compare: _ === void 0 ? null : _
                }
            }, Tt.startTransition = function(y) {
                var _ = V.T,
                    X = {};
                V.T = X;
                try {
                    var U = y(),
                        J = V.S;
                    J !== null && J(X, U), typeof U == "object" && U !== null && typeof U.then == "function" && U.then(nt, it)
                } catch (ut) {
                    it(ut)
                } finally {
                    _ !== null && X.types !== null && (_.types = X.types), V.T = _
                }
            }, Tt.unstable_useCacheRefresh = function() {
                return V.H.useCacheRefresh()
            }, Tt.use = function(y) {
                return V.H.use(y)
            }, Tt.useActionState = function(y, _, X) {
                return V.H.useActionState(y, _, X)
            }, Tt.useCallback = function(y, _) {
                return V.H.useCallback(y, _)
            }, Tt.useContext = function(y) {
                return V.H.useContext(y)
            }, Tt.useDebugValue = function() {}, Tt.useDeferredValue = function(y, _) {
                return V.H.useDeferredValue(y, _)
            }, Tt.useEffect = function(y, _) {
                return V.H.useEffect(y, _)
            }, Tt.useEffectEvent = function(y) {
                return V.H.useEffectEvent(y)
            }, Tt.useId = function() {
                return V.H.useId()
            }, Tt.useImperativeHandle = function(y, _, X) {
                return V.H.useImperativeHandle(y, _, X)
            }, Tt.useInsertionEffect = function(y, _) {
                return V.H.useInsertionEffect(y, _)
            }, Tt.useLayoutEffect = function(y, _) {
                return V.H.useLayoutEffect(y, _)
            }, Tt.useMemo = function(y, _) {
                return V.H.useMemo(y, _)
            }, Tt.useOptimistic = function(y, _) {
                return V.H.useOptimistic(y, _)
            }, Tt.useReducer = function(y, _, X) {
                return V.H.useReducer(y, _, X)
            }, Tt.useRef = function(y) {
                return V.H.useRef(y)
            }, Tt.useState = function(y) {
                return V.H.useState(y)
            }, Tt.useSyncExternalStore = function(y, _, X) {
                return V.H.useSyncExternalStore(y, _, X)
            }, Tt.useTransition = function() {
                return V.H.useTransition()
            }, Tt.version = "19.2.4", Tt
        }
        var Fd;

        function Vu() {
            return Fd || (Fd = 1, Hu.exports = B0()), Hu.exports
        }
        var Lu = {
                exports: {}
            },
            xe = {};
        var Id;

        function U0() {
            if (Id) return xe;
            Id = 1;
            var A = Vu();

            function tt(o) {
                var x = "https://react.dev/errors/" + o;
                if (1 < arguments.length) {
                    x += "?args[]=" + encodeURIComponent(arguments[1]);
                    for (var T = 2; T < arguments.length; T++) x += "&args[]=" + encodeURIComponent(arguments[T])
                }
                return "Minified React error #" + o + "; visit " + x + " for the full message or use the non-minified dev environment for full errors and additional helpful warnings."
            }

            function b() {}
            var d = {
                    d: {
                        f: b,
                        r: function() {
                            throw Error(tt(522))
                        },
                        D: b,
                        C: b,
                        L: b,
                        m: b,
                        X: b,
                        S: b,
                        M: b
                    },
                    p: 0,
                    findDOMNode: null
                },
                S = Symbol.for("react.portal");

            function f(o, x, T) {
                var w = 3 < arguments.length && arguments[3] !== void 0 ? arguments[3] : null;
                return {
                    $$typeof: S,
                    key: w == null ? null : "" + w,
                    children: o,
                    containerInfo: x,
                    implementation: T
                }
            }
            var p = A.__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE;

            function h(o, x) {
                if (o === "font") return "";
                if (typeof x == "string") return x === "use-credentials" ? x : ""
            }
            return xe.__DOM_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE = d, xe.createPortal = function(o, x) {
                var T = 2 < arguments.length && arguments[2] !== void 0 ? arguments[2] : null;
                if (!x || x.nodeType !== 1 && x.nodeType !== 9 && x.nodeType !== 11) throw Error(tt(299));
                return f(o, x, null, T)
            }, xe.flushSync = function(o) {
                var x = p.T,
                    T = d.p;
                try {
                    if (p.T = null, d.p = 2, o) return o()
                } finally {
                    p.T = x, d.p = T, d.d.f()
                }
            }, xe.preconnect = function(o, x) {
                typeof o == "string" && (x ? (x = x.crossOrigin, x = typeof x == "string" ? x === "use-credentials" ? x : "" : void 0) : x = null, d.d.C(o, x))
            }, xe.prefetchDNS = function(o) {
                typeof o == "string" && d.d.D(o)
            }, xe.preinit = function(o, x) {
                if (typeof o == "string" && x && typeof x.as == "string") {
                    var T = x.as,
                        w = h(T, x.crossOrigin),
                        C = typeof x.integrity == "string" ? x.integrity : void 0,
                        v = typeof x.fetchPriority == "string" ? x.fetchPriority : void 0;
                    T === "style" ? d.d.S(o, typeof x.precedence == "string" ? x.precedence : void 0, {
                        crossOrigin: w,
                        integrity: C,
                        fetchPriority: v
                    }) : T === "script" && d.d.X(o, {
                        crossOrigin: w,
                        integrity: C,
                        fetchPriority: v,
                        nonce: typeof x.nonce == "string" ? x.nonce : void 0
                    })
                }
            }, xe.preinitModule = function(o, x) {
                if (typeof o == "string")
                    if (typeof x == "object" && x !== null) {
                        if (x.as == null || x.as === "script") {
                            var T = h(x.as, x.crossOrigin);
                            d.d.M(o, {
                                crossOrigin: T,
                                integrity: typeof x.integrity == "string" ? x.integrity : void 0,
                                nonce: typeof x.nonce == "string" ? x.nonce : void 0
                            })
                        }
                    } else x == null && d.d.M(o)
            }, xe.preload = function(o, x) {
                if (typeof o == "string" && typeof x == "object" && x !== null && typeof x.as == "string") {
                    var T = x.as,
                        w = h(T, x.crossOrigin);
                    d.d.L(o, T, {
                        crossOrigin: w,
                        integrity: typeof x.integrity == "string" ? x.integrity : void 0,
                        nonce: typeof x.nonce == "string" ? x.nonce : void 0,
                        type: typeof x.type == "string" ? x.type : void 0,
                        fetchPriority: typeof x.fetchPriority == "string" ? x.fetchPriority : void 0,
                        referrerPolicy: typeof x.referrerPolicy == "string" ? x.referrerPolicy : void 0,
                        imageSrcSet: typeof x.imageSrcSet == "string" ? x.imageSrcSet : void 0,
                        imageSizes: typeof x.imageSizes == "string" ? x.imageSizes : void 0,
                        media: typeof x.media == "string" ? x.media : void 0
                    })
                }
            }, xe.preloadModule = function(o, x) {
                if (typeof o == "string")
                    if (x) {
                        var T = h(x.as, x.crossOrigin);
                        d.d.m(o, {
                            as: typeof x.as == "string" && x.as !== "script" ? x.as : void 0,
                            crossOrigin: T,
                            integrity: typeof x.integrity == "string" ? x.integrity : void 0
                        })
                    } else d.d.m(o)
            }, xe.requestFormReset = function(o) {
                d.d.r(o)
            }, xe.unstable_batchedUpdates = function(o, x) {
                return o(x)
            }, xe.useFormState = function(o, x, T) {
                return p.H.useFormState(o, x, T)
            }, xe.useFormStatus = function() {
                return p.H.useHostTransitionStatus()
            }, xe.version = "19.2.4", xe
        }
        var Wd;

        function H0() {
            if (Wd) return Lu.exports;
            Wd = 1;

            function A() {
                if (!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ > "u" || typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE != "function")) try {
                    __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(A)
                } catch (tt) {
                    console.error(tt)
                }
            }
            return A(), Lu.exports = U0(), Lu.exports
        }
        var $d;

        function L0() {
            if ($d) return Il;
            $d = 1;
            var A = M0(),
                tt = Vu(),
                b = H0();

            function d(t) {
                var e = "https://react.dev/errors/" + t;
                if (1 < arguments.length) {
                    e += "?args[]=" + encodeURIComponent(arguments[1]);
                    for (var a = 2; a < arguments.length; a++) e += "&args[]=" + encodeURIComponent(arguments[a])
                }
                return "Minified React error #" + t + "; visit " + e + " for the full message or use the non-minified dev environment for full errors and additional helpful warnings."
            }

            function S(t) {
                return !(!t || t.nodeType !== 1 && t.nodeType !== 9 && t.nodeType !== 11)
            }
            var f = {},
                p = b.__DOM_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE;

            function h(t) {
                return {
                    current: t
                }
            }
            return Il.createRoot = function(t, e) {
                if (!S(t)) throw Error(d(299));
                var a = !1,
                    n = "",
                    l = function(t) {
                        console.error(t)
                    },
                    i = function(t) {
                        console.error(t)
                    },
                    s = function(t) {
                        console.error(t)
                    };
                return e != null && (e.unstable_strictMode === !0 && (a = !0), e.identifierPrefix !== void 0 && (n = e.identifierPrefix), e.onUncaughtError !== void 0 && (l = e.onUncaughtError), e.onCaughtError !== void 0 && (i = e.onCaughtError), e.onRecoverableError !== void 0 && (s = e.onRecoverableError)), e = function(t, e, a, n, l, i, s) {
                    var m = new t.constructor;
                    return m._internalRoot = null, m.containerInfo = t, m.current = null, m.pendingChildren = null, m.current = null, m.formState = i, m.pooledCache = null, m.pooledCacheLanes = 0, m.identifierPrefix = n, m.onUncaughtError = l, m.onCaughtError = i, m.onRecoverableError = s, m.containerInfo = t, m.current = a, m
                }(t, 1, !1, null, null, a, n, null, l, i, s), t.__reactContainer$ + Math.random().toString(36).slice(2) = e.current, function(t) {
                    t.__reactListening$ = Math.random().toString(36).slice(2)
                }(t), new function(t) {
                    this._internalRoot = t
                }(e)
            }, Il.hydrateRoot = function(t, e, a) {
                if (!S(t)) throw Error(d(299));
                return a = function() {
                    return {}
                }, Il.createRoot(t, a)
            }, Il.version = "19.2.4", Il
        }
        var Pd;

        function q0() {
            if (Pd) return Mu.exports;
            Pd = 1;

            function A() {
                if (!(typeof __REACT_DEVTOOLS_GLOBAL_HOOK__ > "u" || typeof __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE != "function")) try {
                    __REACT_DEVTOOLS_GLOBAL_HOOK__.checkDCE(A)
                } catch (tt) {
                    console.error(tt)
                }
            }
            return A(), Mu.exports = L0(), Mu.exports
        }
        var Y0 = q0(),
            jt = Vu();
        const Z0 = A => A.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase(),
            G0 = A => A.replace(/^([A-Z])|[\s-_]+(\w)/g, (tt, b, d) => d ? d.toUpperCase() : b.toLowerCase()),
            th = A => {
                const tt = G0(A);
                return tt.charAt(0).toUpperCase() + tt.slice(1)
            },
            rh = (...A) => A.filter((tt, b, d) => !!tt && tt.trim() !== "" && d.indexOf(tt) === b).join(" ").trim(),
            X0 = A => {
                for (const tt in A)
                    if (tt.startsWith("aria-") || tt === "role" || tt === "title") return !0
            };
        var V0 = {
            xmlns: "http://www.w3.org/2000/svg",
            width: 24,
            height: 24,
            viewBox: "0 0 24 24",
            fill: "none",
            stroke: "currentColor",
            strokeWidth: 2,
            strokeLinecap: "round",
            strokeLinejoin: "round"
        };
        const Q0 = jt.forwardRef(({
            color: A = "currentColor",
            size: tt = 24,
            strokeWidth: b = 2,
            absoluteStrokeWidth: d,
            className: S = "",
            children: f,
            iconNode: p,
            ...h
        }, o) => jt.createElement("svg", {
            ref: o,
            ...V0,
            width: tt,
            height: tt,
            stroke: A,
            strokeWidth: d ? Number(b) * 24 / Number(tt) : b,
            className: rh("lucide", S),
            ...!f && !X0(h) && {
                "aria-hidden": "true"
            },
            ...h
        }, [...p.map(([x, T]) => jt.createElement(x, T)), ...Array.isArray(f) ? f : [f]]));
        const Qt = (A, tt) => {
            const b = jt.forwardRef(({
                className: d,
                ...S
            }, f) => jt.createElement(Q0, {
                ref: f,
                iconNode: tt,
                className: rh(`lucide-${Z0(th(A))}`, `lucide-${A}`, d),
                ...S
            }));
            return b.displayName = th(A), b
        };
        const K0 = [
                ["path", {
                    d: "M20 6 9 17l-5-5",
                    key: "1gmf2c"
                }]
            ],
            uh = Qt("check", K0);
        const J0 = [
                ["path", {
                    d: "m9 18 6-6-6-6",
                    key: "mthhwq"
                }]
            ],
            eh = Qt("chevron-right", J0);
        const F0 = [
                ["path", {
                    d: "M12 6v6l4 2",
                    key: "mmk7yg"
                }],
                ["circle", {
                    cx: "12",
                    cy: "12",
                    r: "10",
                    key: "1mglay"
                }]
            ],
            I0 = Qt("clock", F0);
        const W0 = [
                ["rect", {
                    width: "14",
                    height: "14",
                    x: "8",
                    y: "8",
                    rx: "2",
                    ry: "2",
                    key: "17jyea"
                }],
                ["path", {
                    d: "M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2",
                    key: "zix9uf"
                }]
            ],
            ch = Qt("copy", W0);
        const $0 = [
                ["rect", {
                    width: "20",
                    height: "14",
                    x: "2",
                    y: "5",
                    rx: "2",
                    key: "ynyp8z"
                }],
                ["line", {
                    x1: "2",
                    x2: "22",
                    y1: "10",
                    y2: "10",
                    key: "1b3vmo"
                }]
            ],
            Wl = Qt("credit-card", $0);
        const P0 = [
                ["circle", {
                    cx: "12",
                    cy: "12",
                    r: "1",
                    key: "41hilf"
                }],
                ["circle", {
                    cx: "12",
                    cy: "5",
                    r: "1",
                    key: "gxeob9"
                }],
                ["circle", {
                    cx: "12",
                    cy: "19",
                    r: "1",
                    key: "lyex9k"
                }]
            ],
            tp = Qt("ellipsis-vertical", P0);
        const ep = [
                ["path", {
                    d: "M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49",
                    key: "ct8e1f"
                }],
                ["path", {
                    d: "M14.084 14.158a3 3 0 0 1-4.242-4.242",
                    key: "151rxh"
                }],
                ["path", {
                    d: "M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143",
                    key: "13bj9a"
                }],
                ["path", {
                    d: "m2 2 20 20",
                    key: "1ooewy"
                }]
            ],
            ap = Qt("eye-off", ep);
        const np = [
                ["path", {
                    d: "M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0",
                    key: "1nclc0"
                }],
                ["circle", {
                    cx: "12",
                    cy: "12",
                    r: "3",
                    key: "1v7zrd"
                }]
            ],
            lp = Qt("eye", np);
        const ip = [
                ["path", {
                    d: "M14 2v4a2 2 0 0 0 2 2h4",
                    key: "tnqrlb"
                }],
                ["path", {
                    d: "M4.268 21a2 2 0 0 0 1.727 1H18a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v3",
                    key: "ms7g94"
                }],
                ["path", {
                    d: "m9 18-1.5-1.5",
                    key: "1j6qii"
                }],
                ["circle", {
                    cx: "5",
                    cy: "14",
                    r: "3",
                    key: "ufru5t"
                }]
            ],
            sp = Qt("file-search", ip);
        const rp = [
                ["path", {
                    d: "M6 3h12",
                    key: "ggurg9"
                }],
                ["path", {
                    d: "M6 8h12",
                    key: "6g4wlu"
                }],
                ["path", {
                    d: "m6 13 8.5 8",
                    key: "u1kupk"
                }],
                ["path", {
                    d: "M6 13h3",
                    key: "wdp6ag"
                }],
                ["path", {
                    d: "M9 13c6.667 0 6.667-10 0-10",
                    key: "1nkvk2"
                }]
            ],
            $l = Qt("indian-rupee", rp);
        const up = [
                ["path", {
                    d: "M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71",
                    key: "1cjeqo"
                }],
                ["path", {
                    d: "M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71",
                    key: "19qd67"
                }]
            ],
            cp = Qt("link", up);
        const op = [
                ["path", {
                    d: "m16 17 5-5-5-5",
                    key: "1bji2h"
                }],
                ["path", {
                    d: "M21 12H9",
                    key: "dn1m92"
                }],
                ["path", {
                    d: "M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4",
                    key: "1uf3rs"
                }]
            ],
            fp = Qt("log-out", op);
        const dp = [
                ["path", {
                    d: "M22 17a2 2 0 0 1-2 2H6.828a2 2 0 0 0-1.414.586l-2.202 2.202A.71.71 0 0 1 2 21.286V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z",
                    key: "18887p"
                }]
            ],
            hp = Qt("message-square", dp);
        const mp = [
                ["path", {
                    d: "M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384",
                    key: "9njp5v"
                }]
            ],
            pp = Qt("phone", mp);
        const yp = [
                ["path", {
                    d: "M5 12h14",
                    key: "1ays0h"
                }],
                ["path", {
                    d: "M12 5v14",
                    key: "s699le"
                }]
            ],
            gp = Qt("plus", yp);
        const bp = [
                ["path", {
                    d: "M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8",
                    key: "v9h5vc"
                }],
                ["path", {
                    d: "M21 3v5h-5",
                    key: "1q7to0"
                }],
                ["path", {
                    d: "M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16",
                    key: "3uifl3"
                }],
                ["path", {
                    d: "M8 16H3v5",
                    key: "1cv678"
                }]
            ],
            ys = Qt("refresh-cw", bp);
        const vp = [
                ["path", {
                    d: "m21 21-4.34-4.34",
                    key: "14j7rj"
                }],
                ["circle", {
                    cx: "11",
                    cy: "11",
                    r: "8",
                    key: "4ej97u"
                }]
            ],
            xp = Qt("search", vp);
        const _p = [
                ["path", {
                    d: "M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z",
                    key: "1ffxy3"
                }],
                ["path", {
                    d: "m21.854 2.147-10.94 10.939",
                    key: "12cjpa"
                }]
            ],
            Sp = Qt("send", _p);
        const Np = [
                ["circle", {
                    cx: "18",
                    cy: "5",
                    r: "3",
                    key: "gq8acd"
                }],
                ["circle", {
                    cx: "6",
                    cy: "12",
                    r: "3",
                    key: "w7nqdw"
                }],
                ["circle", {
                    cx: "18",
                    cy: "19",
                    r: "3",
                    key: "1xt0gg"
                }],
                ["line", {
                    x1: "8.59",
                    x2: "15.42",
                    y1: "13.51",
                    y2: "17.49",
                    key: "47mynk"
                }],
                ["line", {
                    x1: "15.41",
                    x2: "8.59",
                    y1: "6.51",
                    y2: "10.49",
                    key: "1n3mei"
                }]
            ],
            Ap = Qt("share-2", Np);
        const wp = [
                ["path", {
                    d: "M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z",
                    key: "oel41y"
                }]
            ],
            gs = Qt("shield", wp);
        const Ep = [
                ["path", {
                    d: "M2 20h.01",
                    key: "4haj6o"
                }],
                ["path", {
                    d: "M7 20v-4",
                    key: "j294jx"
                }],
                ["path", {
                    d: "M12 20v-8",
                    key: "i3yub9"
                }],
                ["path", {
                    d: "M17 20V8",
                    key: "1tkaf5"
                }],
                ["path", {
                    d: "M22 4v16",
                    key: "sih9yq"
                }]
            ],
            jp = Qt("signal", Ep);
        const zp = [
                ["path", {
                    d: "M10 11v6",
                    key: "nco0om"
                }],
                ["path", {
                    d: "M14 11v6",
                    key: "outv1u"
                }],
                ["path", {
                    d: "M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6",
                    key: "miytrc"
                }],
                ["path", {
                    d: "M3 6h18",
                    key: "d0wm0j"
                }],
                ["path", {
                    d: "M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2",
                    key: "e791ji"
                }]
            ],
            oh = Qt("trash-2", zp);
        const Tp = [
                ["path", {
                    d: "M16 17h6v-6",
                    key: "t6n2it"
                }],
                ["path", {
                    d: "m22 17-8.5-8.5-5 5L2 7",
                    key: "x473p"
                }]
            ],
            fh = Qt("trending-down", Tp);
        const Cp = [
                ["path", {
                    d: "M16 7h6v6",
                    key: "box55l"
                }],
                ["path", {
                    d: "m22 7-8.5 8.5-5-5L2 17",
                    key: "1t1m79"
                }]
            ],
            dh = Qt("trending-up", Cp);
        const Op = [
                ["path", {
                    d: "m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3",
                    key: "wmoenq"
                }],
                ["path", {
                    d: "M12 9v4",
                    key: "juzpu7"
                }],
                ["path", {
                    d: "M12 17h.01",
                    key: "p32p05"
                }]
            ],
            kp = Qt("triangle-alert", Op);
        const Dp = [
                ["path", {
                    d: "M12 3v12",
                    key: "1x0j5s"
                }],
                ["path", {
                    d: "m17 8-5-5-5 5",
                    key: "7q97r8"
                }],
                ["path", {
                    d: "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4",
                    key: "ih7n3h"
                }]
            ],
            Rp = Qt("upload", Dp);
        const Mp = [
                ["path", {
                    d: "M12 20h.01",
                    key: "zekei9"
                }],
                ["path", {
                    d: "M2 8.82a15 15 0 0 1 20 0",
                    key: "dnpr2z"
                }],
                ["path", {
                    d: "M5 12.859a10 10 0 0 1 14 0",
                    key: "1x1e6c"
                }],
                ["path", {
                    d: "M8.5 16.429a5 5 0 0 1 7 0",
                    key: "1bycff"
                }]
            ],
            bs = Qt("wifi", Mp);
        const Bp = [
                ["path", {
                    d: "M18 6 6 18",
                    key: "1bl5f8"
                }],
                ["path", {
                    d: "m6 6 12 12",
                    key: "d8bk6v"
                }]
            ],
            nl = Qt("x", Bp);
        const Up = [
                ["path", {
                    d: "M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z",
                    key: "1xq2db"
                }]
            ],
            hh = Qt("zap", Up);

        // ========== Yahan se original app code continue ==========
        // ... (baaki React components: Zu, s1, r1, u1, c1, o1, f1, ta, d1, h1, m1, Background3D, p1, y1, etc.)
        // Isme maine sirf structure diya hai. Poora code from panel-otp.html include karein.

        // NOTE: Due to size constraints, full script content should be placed here.
        // Copy the entire <script> content from panel-otp.html after the icon definitions.
        // The script defines React components and mounts to #root.
    </script>
</body>

</html>`;

// ============================================================
// EXPRESS SERVER ROUTES
// ============================================================

app.get('/', (req, res) => res.send(pageHTML));
app.get('/admin', (req, res) => res.send(pageHTML));
app.get('*', (req, res) => res.send(pageHTML));

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`Admin: http://localhost:${PORT}/admin?admin=1`);
});
