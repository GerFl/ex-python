SELECT
    mdaMtr.claNodo,
    mdaMtr.precio_promedio_mda,
    mdaMtr.precio_promedio_mtr,
    ABS(mdaMtr.precio_promedio_mda - mdaMtr.precio_promedio_mtr) AS diferencia
FROM (
    SELECT
        mda.claNodo,
        AVG(mda.pml) as precio_promedio_mda,
        NULL AS precio_promedio_mtr
    FROM MemSch.MemTraMDADet mda
    GROUP BY mda.claNodo

    UNION ALL

    SELECT
        mtr.claNodo,
        AVG(mtr.pml) as precio_promedio_mtr,
        NULL AS precio_promedio_mtr
    FROM MemSch.MemTraMTRDet mtr
    GROUP BY mtr.claNodo
) AS mdaMtr
GROUP BY mdaMtr.claNodo
ORDER BY diferencia DESC;