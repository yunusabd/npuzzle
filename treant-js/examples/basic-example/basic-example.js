// Another approach, same result
// JSON approach

const chart_config = {
  chart: {
    container: '#basic-example',

    connectors: {
      type: 'step',
    },
    node: {
      HTMLclass: 'nodeExample1',
    },
  },
  nodeStructure: {
    innerHTML: '\
    <table>\
      <tr>\
        <td>1</td>\
        <td>2</td>\
        <td>3</td>\
      </tr>\
      <tr>\
        <td>4</td>\
        <td>5</td>\
        <td>6</td>\
      </tr>\
      <tr>\
        <td>7</td>\
        <td>8</td>\
            <td>9</td>\
      </tr>\
    </table>',
    children: [
      {
        text: {
          name: 'Joe Linux',
          title: 'Chief Technology Officer',
        },
        stackChildren: true,
        image: '../headshots/1.jpg',
        children: [
          {
            text: {
              name: 'Ron Blomquist',
              title: 'Chief Information Security Officer',
            },
            image: '../headshots/8.jpg',
          },
          {
            text: {
              name: 'Michael Rubin',
              title: 'Chief Innovation Officer',
              contact: 'we@aregreat.com',
            },
            image: '../headshots/9.jpg',
          },
        ],
      },
      {
        stackChildren: true,
        text: {
          name: 'Linda May',
          title: 'Chief Business Officer',
        },
        image: '../headshots/5.jpg',
        children: [
          {
            text: {
              name: 'Alice Lopez',
              title: 'Chief Communications Officer',
            },
            image: '../headshots/7.jpg',
          },
          {
            text: {
              name: 'Mary Johnson',
              title: 'Chief Brand Officer',
            },
            image: '../headshots/4.jpg',
          },
          {
            text: {
              name: 'Kirk Douglas',
              title: 'Chief Business Development Officer',
            },
            image: '../headshots/11.jpg',
          },
        ],
      },
      {
        text: {
          name: 'John Green',
          title: 'Chief accounting officer',
          contact: 'Tel: 01 213 123 134',
        },
        image: '../headshots/6.jpg',
        children: [
          {
            text: {
              name: 'Erica Reel',
              title: 'Chief Customer Officer',
            },
            link: {
              href: 'http://www.google.com',
            },
            image: '../headshots/10.jpg',
          },
        ],
      },
    ],
  },
};
