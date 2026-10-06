"""Initial schema for AI City Command Center

Revision ID: 20261006_initial
Revises: 
Create Date: 2026-10-06 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


revision = '20261006_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'zones',
        sa.Column('zone_id', sa.String(length=40), nullable=False),
        sa.Column('name', sa.String(length=120), nullable=False),
        sa.Column('district', sa.String(length=120), nullable=False),
        sa.Column('criticality_weight', sa.Float(), nullable=False),
        sa.Column('status', sa.String(length=50), nullable=False),
        sa.Column('center_latitude', sa.Float(), nullable=False),
        sa.Column('center_longitude', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('zone_id'),
        sa.UniqueConstraint('name'),
    )
    op.create_index(op.f('ix_zones_zone_id'), 'zones', ['zone_id'], unique=False)

    op.create_table(
        'incidents',
        sa.Column('incident_id', sa.String(length=64), nullable=False),
        sa.Column('zone_id', sa.String(length=40), nullable=True),
        sa.Column('title', sa.String(length=150), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('category', sa.String(length=50), nullable=False),
        sa.Column('severity', sa.String(length=20), nullable=False),
        sa.Column('status', sa.String(length=30), nullable=False),
        sa.Column('latitude', sa.Float(), nullable=False),
        sa.Column('longitude', sa.Float(), nullable=False),
        sa.Column('source_type', sa.String(length=40), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['zone_id'], ['zones.zone_id']),
        sa.PrimaryKeyConstraint('incident_id'),
        sa.CheckConstraint('latitude BETWEEN -90 AND 90', name='incident_lat_range'),
        sa.CheckConstraint('longitude BETWEEN -180 AND 180', name='incident_lon_range'),
    )
    op.create_index(op.f('ix_incidents_incident_id'), 'incidents', ['incident_id'], unique=False)
    op.create_index(op.f('ix_incidents_zone_id'), 'incidents', ['zone_id'], unique=False)

    op.create_table(
        'ai_analysis_results',
        sa.Column('analysis_id', sa.String(length=64), nullable=False),
        sa.Column('incident_id', sa.String(length=64), nullable=False),
        sa.Column('detected', sa.Boolean(), nullable=False),
        sa.Column('suggested_category', sa.String(length=50), nullable=False),
        sa.Column('confidence_score', sa.Float(), nullable=False),
        sa.Column('hazard_features', sa.JSON(), nullable=True),
        sa.Column('recommended_action', sa.String(length=120), nullable=False),
        sa.Column('inference_mode', sa.String(length=40), nullable=False),
        sa.Column('latency_ms', sa.Float(), nullable=False),
        sa.Column('analyzed_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['incident_id'], ['incidents.incident_id']),
        sa.PrimaryKeyConstraint('analysis_id'),
    )
    op.create_index(op.f('ix_ai_analysis_results_analysis_id'), 'ai_analysis_results', ['analysis_id'], unique=False)
    op.create_index(op.f('ix_ai_analysis_results_incident_id'), 'ai_analysis_results', ['incident_id'], unique=False)

    op.create_table(
        'alerts',
        sa.Column('alert_id', sa.String(length=64), nullable=False),
        sa.Column('incident_id', sa.String(length=64), nullable=False),
        sa.Column('severity', sa.String(length=20), nullable=False),
        sa.Column('headline', sa.String(length=120), nullable=False),
        sa.Column('message', sa.Text(), nullable=False),
        sa.Column('is_acknowledged', sa.Boolean(), nullable=False),
        sa.Column('triggered_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['incident_id'], ['incidents.incident_id']),
        sa.PrimaryKeyConstraint('alert_id'),
    )
    op.create_index(op.f('ix_alerts_alert_id'), 'alerts', ['alert_id'], unique=False)
    op.create_index(op.f('ix_alerts_incident_id'), 'alerts', ['incident_id'], unique=False)

    op.create_table(
        'response_logs',
        sa.Column('response_id', sa.String(length=64), nullable=False),
        sa.Column('incident_id', sa.String(length=64), nullable=False),
        sa.Column('stage', sa.String(length=30), nullable=False),
        sa.Column('assigned_agency', sa.String(length=120), nullable=True),
        sa.Column('assigned_unit', sa.String(length=120), nullable=True),
        sa.Column('action_note', sa.Text(), nullable=True),
        sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['incident_id'], ['incidents.incident_id']),
        sa.PrimaryKeyConstraint('response_id'),
    )
    op.create_index(op.f('ix_response_logs_response_id'), 'response_logs', ['response_id'], unique=False)
    op.create_index(op.f('ix_response_logs_incident_id'), 'response_logs', ['incident_id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_response_logs_incident_id'), table_name='response_logs')
    op.drop_index(op.f('ix_response_logs_response_id'), table_name='response_logs')
    op.drop_table('response_logs')

    op.drop_index(op.f('ix_alerts_incident_id'), table_name='alerts')
    op.drop_index(op.f('ix_alerts_alert_id'), table_name='alerts')
    op.drop_table('alerts')

    op.drop_index(op.f('ix_ai_analysis_results_incident_id'), table_name='ai_analysis_results')
    op.drop_index(op.f('ix_ai_analysis_results_analysis_id'), table_name='ai_analysis_results')
    op.drop_table('ai_analysis_results')

    op.drop_index(op.f('ix_incidents_zone_id'), table_name='incidents')
    op.drop_index(op.f('ix_incidents_incident_id'), table_name='incidents')
    op.drop_table('incidents')

    op.drop_index(op.f('ix_zones_zone_id'), table_name='zones')
    op.drop_table('zones')
