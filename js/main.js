$(document).ready(function () {
  $("#canvas-container").vfireworks({
    launchTime: 20230000, // 烟花持续时间，毫秒
    clickLaunch: true, // 鼠标点击是否触发烟花
    showRoute: true, // 是否显示发射路径
    fworkSpeed: 1, // 发射速度，值越大越快
    fworkAccel: 4, // 发射加速度
    partCount: 165, // 炸裂后分散数量
    partSpeed: 4, // 炸裂后分散速度，值越大分散越大
    partSpeedVariance: 1, // 炸裂分散变化幅度，值越大越接近直线
    partFriction: 3, // 炸裂阻力，值越大炸裂分散越小
    partGravity: 1, // 引力，负值是反重力，正值越大受重力影响越大
    hueMin: 0, // 色调最小值
    hueMax: 255, // 色调最大值
    hueVariance: 255, // 色调变化幅度，值越大颜色越丰富
    lineWidth: 1, // 烟花效果粗细
    clearAlpha: 25, // 视觉残留效果，值越大痕迹残留时间越短，值为 0 是烟花发射和炸裂痕迹不消失
  });
});
